# pylint: disable=line-too-long, missing-function-docstring
"""
gpxtable - Create a markdown template from a Garmin GPX file for route information
"""

import math
import re
from datetime import datetime, timedelta
from typing import Optional, Union, List, NamedTuple, TextIO

import astral
import astral.sun
import gpxpy.gpx
import gpxpy.geo
import gpxpy.utils

KM_TO_MILES = 0.621371
M_TO_FEET = 3.28084


class NearestLocationDataExt(NamedTuple):
    """
    Extended class for gpxpy.gpx.NearestLocationData

    Includes distance_from_start
    """

    location: "gpxpy.gpx.GPXTrackPoint"
    track_no: int
    segment_no: int
    point_no: int
    distance_from_start: float


class GPXTrackExt(gpxpy.gpx.GPXTrack):
    """
    Extended class for gpxpy.gpx.GPXTrack

    usage: ext_track = GPXTrackExt(track)
    """

    def __init__(self, track):  # pylint: disable=super-init-not-called
        self.gpx_track = track

    def get_points_data(self, distance_2d: bool = False) -> List[gpxpy.gpx.PointData]:
        """
        Returns a list of tuples containing the actual point, its distance from the start,
        track_no, segment_no, and segment_point_no
        """
        distance_from_start = 0.0
        previous_point = None

        # (point, distance_from_start) pairs:
        points = []

        for segment_no, segment in enumerate(self.gpx_track.segments):
            for point_no, point in enumerate(segment.points):
                if previous_point and point_no > 0:
                    if distance_2d:
                        distance = point.distance_2d(previous_point)
                    else:
                        distance = point.distance_3d(previous_point)

                    distance_from_start += distance or 0.0

                points.append(
                    gpxpy.gpx.PointData(
                        point, distance_from_start, -1, segment_no, point_no
                    )
                )

                previous_point = point

        return points

    def get_nearest_locations(
        self,
        location: gpxpy.geo.Location,
        threshold_distance: float = 0.01,
        deduplicate_distance: float = 0.0,
    ) -> List[NearestLocationDataExt]:
        # pylint: disable=too-many-locals
        """
        Returns a list of locations of elements like
        consisting of points where the location may be on the track

        threshold_distance is the minimum distance from the track
        so that the point *may* be counted as to be "on the track".
        For example 0.01 means 1% of the track distance.

        deduplicate_distance is an actual distance in meters, not a
        ratio based upon threshold. 2000 means it will not return
        duplicates within 2km in case the track wraps around itself.
        """

        def _deduplicate(
            locations: List[NearestLocationDataExt], delta: float = 0.0
        ) -> List[NearestLocationDataExt]:
            previous: Optional[NearestLocationDataExt] = None
            filtered: List[NearestLocationDataExt] = []
            for point in locations:
                if (
                    not previous
                    or (point.distance_from_start - previous.distance_from_start)
                    > delta
                ):
                    filtered.append(point)
                previous = point
            return filtered

        assert location
        assert threshold_distance

        result: List[NearestLocationDataExt] = []

        points = self.get_points_data()

        if not points:
            return result

        distance: Optional[float] = points[-1][1]

        threshold = (distance or 0.0) * threshold_distance

        min_distance_candidate: Optional[float] = None
        distance_from_start_candidate: Optional[float] = None
        track_no_candidate: Optional[int] = None
        segment_no_candidate: Optional[int] = None
        point_no_candidate: Optional[int] = None
        point_candidate: Optional[gpxpy.gpx.GPXTrackPoint] = None

        for point, distance_from_start, track_no, segment_no, point_no in points:
            distance = location.distance_3d(point) or math.inf
            if distance < threshold:
                if min_distance_candidate is None or distance < min_distance_candidate:
                    min_distance_candidate = distance
                    distance_from_start_candidate = distance_from_start
                    track_no_candidate = track_no
                    segment_no_candidate = segment_no
                    point_no_candidate = point_no
                    point_candidate = point
            else:
                if (
                    distance_from_start_candidate is not None
                    and point_candidate is not None
                    and track_no_candidate is not None
                    and segment_no_candidate is not None
                    and point_no_candidate is not None
                ):
                    result.append(
                        NearestLocationDataExt(
                            point_candidate,
                            track_no_candidate,
                            segment_no_candidate,
                            point_no_candidate,
                            distance_from_start_candidate,
                        )
                    )
                min_distance_candidate = None
                distance_from_start_candidate = None
                track_no_candidate = None
                segment_no_candidate = None
                point_no_candidate = None
                point_candidate = None

        if (
            distance_from_start_candidate is not None
            and point_candidate is not None
            and track_no_candidate is not None
            and segment_no_candidate is not None
            and point_no_candidate is not None
        ):
            result.append(
                NearestLocationDataExt(
                    point_candidate,
                    track_no_candidate,
                    segment_no_candidate,
                    point_no_candidate,
                    distance_from_start_candidate,
                )
            )
        return _deduplicate(result, deduplicate_distance)


class GPXTableCalculator:
    """
    Create a waypoint/route-point table based upon GPX information.

    :param gpxpy.gpx.GPX gpx: gpxpy gpx data
    :param TextIO output: output stream or (stdio if not specified)
    :param bool imperial: display in Imperial units (default imperial)
    :param float speed: optional speed of travel for time-distance calculations
    :param datetime depart_at: if provided, departure time for route or tracks to start
    :param bool ignore_times: ignore any timestamps in provided GPX routes or tracks
    :param bool display_coordinates: include latitude and longitude of points in table
    """

    #: 200m allowed between waypoint and start/end of track
    waypoint_delta = 200.0

    #: 10km between duplicates of the same waypoint on a track
    waypoint_debounce = 10000.0

    #: Assume traveling at 30mph/50kph
    default_travel_speed = 30.0 / KM_TO_MILES

    #: dict: Add a layover time automatically if a waypoint symbol matches
    waypoint_delays = {
        "Restaurant": timedelta(minutes=60),
        "Gas Station": timedelta(minutes=15),
        "Restroom": timedelta(minutes=15),
        "Photo": timedelta(minutes=5),
        "Scenic Area": timedelta(minutes=5),
    }

    LLP_HDR = "|        Lat,Lon       "
    LLP_SEP = "| :------------------: "
    LLP_FMT = "| {:-10.4f},{:.4f} "
    OUT_HDR = "| Name                           |   Dist. | G |  ETA  | Notes"
    OUT_SEP = "| :----------------------------- | ------: | - | ----: | :----"
    OUT_FMT = "| {:30.30} | {:>7} | {:1} | {:>5} | {}{}"

    XML_NAMESPACE = {
        "trp": "http://www.garmin.com/xmlschemas/TripExtensions/v1",
        "gpxx": "http://www.garmin.com/xmlschemas/GpxExtensions/v3",
    }

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        gpx: gpxpy.gpx.GPX,
        output: Optional[TextIO] = None,
        imperial: bool = True,
        speed: float = 30.0 / KM_TO_MILES,
        depart_at: Optional[datetime] = None,
        ignore_times: bool = False,
        display_coordinates: bool = False,
    ) -> None:
        self.gpx = gpx
        self.output = output
        self.speed = (
            speed / KM_TO_MILES if imperial else speed
        ) or self.default_travel_speed
        self.imperial: bool = imperial
        self.depart_at: Optional[datetime] = depart_at
        self.ignore_times: bool = ignore_times
        self.display_coordinates: bool = display_coordinates

    def print_all(self) -> None:
        """
        Output full combination of header, waypoints, and routes.
        """
        self.print_header()
        self.print_waypoints()
        self.print_routes()

    def print_header(self) -> None:
        """
        Print to stream generic information about the GPX data such as name, creator, and calculation
        variables.
        """
        if self.gpx.name:
            print(f"## {self.gpx.name}", file=self.output)
        if self.gpx.creator:
            print(f"* {self.gpx.creator}", file=self.output)
        if self.depart_at:
            print(f"* Departure at {self.depart_at:%c}", file=self.output)
        move_data = self.gpx.get_moving_data()
        if move_data and move_data.moving_time:
            print(
                f"* Total moving time: {self._format_time(move_data.moving_time, False)}",
                file=self.output,
            )
        dist = self.gpx.length_2d()
        if dist:
            print(
                f"* Total distance: {self._format_long_length(dist, True)}",
                file=self.output,
            )
        if self.speed:
            print(
                f"* Default speed: {self._format_speed(self.speed, True)}",
                file=self.output,
            )

    def _populate_times(self) -> None:
        if not self.depart_at or not self.speed:
            return
        for track_no, track in enumerate(self.gpx.tracks):
            # assume (for now) that if there are multiple tracks, 1 track = 1 day
            depart_at = self.depart_at + timedelta(hours=24 * track_no)
            time_bounds = track.get_time_bounds()
            # handle the case where the GPX generator is putting crap for times in the tracks (basecamp)
            if self.ignore_times or time_bounds.start_time == time_bounds.end_time:
                track.remove_time()
            time_bounds = track.get_time_bounds()
            # if track has legitimate times in it, just adjust our delta for departure
            if time_bounds.start_time:
                track.adjust_time(depart_at - time_bounds.start_time)
            else:
                track.segments[0].points[0].time = depart_at
                track.segments[-1].points[-1].time = depart_at + timedelta(
                    hours=track.length_2d() / (self.speed * 1000)
                )
        self.gpx.add_missing_times()

    def print_waypoints(self) -> None:
        """
        Print waypoint information

        Look for all the waypoints associated with tracks present to attempt to reconstruct
        the order and distance of the waypoints. If a departure time has been set, estimate
        the arrival time at each waypoint and probable layover times.
        """

        def _wpe() -> str:
            final_waypoint = (
                abs(track_point.distance_from_start - track_length)
                < self.waypoint_delta
            )
            result = ""
            if self.display_coordinates:
                result += self.LLP_FMT.format(waypoint.latitude, waypoint.longitude)
            return result + self.OUT_FMT.format(
                (waypoint.name or "").replace("\n", " "),
                (
                    f"{self._format_long_length(round(track_point.distance_from_start - last_gas))}/{self._format_long_length(round(track_point.distance_from_start))}"
                    if self._is_gas(waypoint) or final_waypoint
                    else f"{self._format_long_length(round(track_point.distance_from_start))}"
                ),
                (
                    self._point_marker(waypoint)
                    if track_point.distance_from_start > self.waypoint_delta
                    and not final_waypoint
                    else ""
                ),
                (
                    (track_point.location.time + waypoint_delays)
                    .astimezone()
                    .strftime("%H:%M")
                    if track_point.location.time
                    else ""
                ),
                waypoint.symbol or "",
                f" (+{str(layover)[:-3]})" if layover else "",
            )

        self._populate_times()
        for track in self.gpx.tracks:
            waypoints = [
                (
                    wp,
                    GPXTrackExt(track).get_nearest_locations(
                        wp, 0.001, deduplicate_distance=self.waypoint_debounce
                    ),
                )
                for wp in self.gpx.waypoints
                if not self._shaping_point(wp)
            ]
            waypoints = sorted(
                [(wp, tp) for wp, tps in waypoints for tp in tps],
                key=lambda entry: entry[1].point_no,
            )
            track_length = track.length_2d()

            print(f"\n## Track: {track.name}", file=self.output)
            if track.description:
                print(f"* {track.description}", file=self.output)
            print(self._format_output_header(), file=self.output)
            waypoint_delays = timedelta()
            last_gas = 0.0

            for waypoint, track_point in waypoints:
                first_waypoint = waypoint == waypoints[0][0]
                last_waypoint = waypoint == waypoints[-1][0]
                if last_gas > track_point.distance_from_start:
                    last_gas = 0.0  # assume we have filled up between track segments
                layover = (
                    timedelta()
                    if first_waypoint or last_waypoint
                    else self._point_delay(waypoint)
                )
                print(_wpe(), file=self.output)
                if self._is_gas(waypoint):
                    last_gas = track_point.distance_from_start
                waypoint_delays += layover
            almanac = self._sun_rise_set(
                track.segments[0].points[0],
                track.segments[-1].points[-1],
                delay=waypoint_delays,
            )
            if almanac:
                print(f"\n* {almanac}", file=self.output)

    def print_routes(self) -> None:
        # pylint: disable=too-many-branches
        """
        Print route points present in GPX routes.

        If Garmin extensions to create "route-tracks" are present will calculate distances, arrival and departure
        times properly. If the route points have symbols encoded properly, will automatically compute layover
        estimates as well as gas stops.
        """

        def _rpe() -> str:
            result = ""
            if self.display_coordinates:
                result += self.LLP_FMT.format(point.latitude, point.longitude)
            return result + self.OUT_FMT.format(
                (point.name or "").replace("\n", " "),
                (
                    f"{self._format_long_length(dist - last_gas)}/{self._format_long_length(dist)}"
                    if self._is_gas(point) or point is route.points[-1]
                    else f"{self._format_long_length(dist)}"
                ),
                (
                    self._point_marker(point)
                    if point not in [route.points[0], route.points[-1]]
                    else ""
                ),
                timing.astimezone().strftime("%H:%M") if timing else "",
                point.symbol or "",
                f" (+{str(delay)[:-3]})" if delay else "",
            )

        for route in self.gpx.routes:
            print(f"\n## Route: {route.name}", file=self.output)
            if route.description:
                print(f"* {route.description}", file=self.output)

            print(self._format_output_header(), file=self.output)
            dist = 0.0
            previous = route.points[0].latitude, route.points[0].longitude
            last_gas = 0.0
            timing = self._departure_time(route.points[0], True)
            delay = timedelta()
            if timing:
                route.points[0].time = timing
            last_display_distance = 0.0
            for point in route.points:
                if not self._shaping_point(point):
                    if timing:
                        timing += self._travel_time(dist - last_display_distance)
                    last_display_distance = dist
                    departure = self._departure_time(point, dist == 0.0)
                    if departure:
                        timing = departure
                    delay = (
                        self._layover(point)
                        if point not in [route.points[0], route.points[-1]]
                        else timedelta()
                    )
                    if last_gas > dist:
                        last_gas = 0.0
                    print(_rpe(), file=self.output)
                    if timing:
                        timing += delay
                if self._is_gas(point):
                    last_gas = dist
                current = point.latitude, point.longitude
                dist += gpxpy.geo.distance(
                    previous[0], previous[1], None, current[0], current[1], None
                )
                for extension in point.extensions:
                    for extension_point in extension.findall(
                        "gpxx:rpt", self.XML_NAMESPACE
                    ):
                        current = float(extension_point.get("lat")), float(
                            extension_point.get("lon")
                        )
                        dist += gpxpy.geo.distance(
                            previous[0], previous[1], None, current[0], current[1], None
                        )
                        previous = current
                previous = current
            if timing:
                route.points[-1].time = timing
            almanac = self._sun_rise_set(route.points[0], route.points[-1])
            if almanac:
                print(f"\n* {almanac}", file=self.output)

    def _format_output_header(self) -> str:
        if self.display_coordinates:
            return f"\n{self.LLP_HDR}{self.OUT_HDR}\n{self.LLP_SEP}{self.OUT_SEP}"
        return f"\n{self.OUT_HDR}\n{self.OUT_SEP}"

    @staticmethod
    def _format_time(time_s: float, seconds: bool) -> str:
        if not time_s:
            return "n/a"
        if seconds:
            return str(int(time_s))
        minutes = math.floor(time_s / 60.0)
        hours = math.floor(minutes / 60.0)
        return f"{int(hours):02d}:{int(minutes % 60):02d}:{int(time_s % 60):02d}"

    def _format_long_length(self, length: float, units: bool = False) -> str:
        if self.imperial:
            return f'{round(length / 1000. * KM_TO_MILES):.0f}{" mi" if units else ""}'
        return f'{round(length / 1000.):.0f}{" km" if units else ""}'

    def _format_short_length(self, length: float, units: bool = False) -> str:
        if self.imperial:
            return f'{length * M_TO_FEET:.2f}{" ft" if units else ""}'
        return f'{length:.2f}{" m" if units else ""}'

    def _format_speed(self, speed: Optional[float], units: bool = False) -> str:
        """speed is in kph"""
        if not speed:
            speed = 0.0
        if self.imperial:
            return f'{speed * KM_TO_MILES:.2f}{" mph" if units else ""}'
        return f'{speed:.2f}{" km/h" if units else ""}'

    def _point_delay(
        self, point: Union[gpxpy.gpx.GPXWaypoint, gpxpy.gpx.GPXRoutePoint]
    ) -> timedelta:
        return (
            (
                self.waypoint_delays.get("Restaurant")
                if self._is_meal(point)
                else timedelta()
            )
            or (
                self.waypoint_delays.get("Gas Station")
                if self._is_gas(point)
                else timedelta()
            )
            or (
                self.waypoint_delays.get("Scenic Area")
                if self._is_scenic_area(point)
                else timedelta()
            )
            or (
                self.waypoint_delays.get("Restroom")
                if self._is_restroom(point)
                else timedelta()
            )
            or self.waypoint_delays.get(point.symbol or "nil")
            or timedelta()
        )

    def _point_marker(
        self, point: Union[gpxpy.gpx.GPXWaypoint, gpxpy.gpx.GPXRoutePoint]
    ) -> str:
        return (
            self._is_meal(point)
            or self._is_gas(point)
            #            or self.is_scenic_area(point)
            #            or self.is_restroom(point)
            or " "
        )

    def _travel_time(self, dist: float) -> timedelta:
        """distance is in meters, speed is in km/h"""
        return timedelta(minutes=dist / 1000.0 / self.speed * 60.0)

    def _layover(self, point: gpxpy.gpx.GPXRoutePoint) -> timedelta:
        """layover time at a given RoutePoint (Basecamp extension)"""
        for extension in point.extensions:
            for duration in extension.findall("trp:StopDuration", self.XML_NAMESPACE):
                match = re.match(r"^PT((\d+)H)?((\d+)M)?$", duration.text)
                if match:
                    return timedelta(
                        hours=int(match.group(2) or "0"),
                        minutes=int(match.group(4) or "0"),
                    )
        return self._point_delay(point)

    def _departure_time(
        self,
        point: Union[
            gpxpy.gpx.GPXWaypoint, gpxpy.gpx.GPXRoutePoint, gpxpy.gpx.GPXTrackPoint
        ],
        use_departure: Optional[bool] = False,
    ) -> Optional[datetime]:
        """returns datetime object for route point with departure times or None"""
        if use_departure and self.depart_at:
            return self.depart_at
        for extension in point.extensions:
            for departure in extension.findall("trp:DepartureTime", self.XML_NAMESPACE):
                return datetime.fromisoformat(departure.text.replace("Z", "+00:00"))
        return None

    def _sun_rise_set(
        self,
        start: Union[gpxpy.gpx.GPXRoutePoint, gpxpy.gpx.GPXTrackPoint],
        end: Union[gpxpy.gpx.GPXRoutePoint, gpxpy.gpx.GPXTrackPoint],
        delay: Optional[timedelta] = None,
    ) -> str:
        """return sunrise/sunset and start & end info based upon the route start and end point"""
        if not start.time or not end.time:
            return ""
        sun_start = astral.sun.sun(
            astral.LocationInfo(
                "Start Point", "", "", start.latitude, start.longitude
            ).observer,
            date=start.time,
        )
        sun_end = astral.sun.sun(
            astral.LocationInfo(
                "End Point", "", "", end.latitude, end.longitude
            ).observer,
            date=end.time + (delay or timedelta()),
        )
        times = {
            "Sunrise": sun_start["sunrise"],
            "Sunset": sun_end["sunset"],
            "Starts": start.time,
            "Ends": end.time + (delay or timedelta()),
        }
        first = True
        retval = f"{start.time.astimezone():%x}: "
        for name, time in sorted(times.items(), key=lambda kv: kv[1]):
            if first is not True:
                retval += ", "
            first = False
            retval += f"{name}: {time.astimezone():%H:%M}"
        return retval

    @staticmethod
    def _is_gas(point: Union[gpxpy.gpx.GPXWaypoint, gpxpy.gpx.GPXRoutePoint]) -> str:
        if (
            point.symbol
            and "Gas Station" in point.symbol
            or re.search(r"\bGas\b|\bFuel\b|\b(G)\b", point.name or "", re.I)
        ):
            if not point.symbol:
                point.symbol = "Gas"
            return "G"
        return ""

    @staticmethod
    def _is_meal(point: Union[gpxpy.gpx.GPXWaypoint, gpxpy.gpx.GPXRoutePoint]) -> str:
        if (
            point.symbol
            and "Restaurant" in point.symbol
            or re.search(
                r"\bRestaurant\b|\bLunch\b|\bBreakfast\b|\b\Dinner\b|\b(L)\b",
                point.name or "",
                re.I,
            )
        ):
            if not point.symbol:
                point.symbol = "Restaurant"
            return "L"
        return ""

    @staticmethod
    def _is_scenic_area(
        point: Union[gpxpy.gpx.GPXWaypoint, gpxpy.gpx.GPXRoutePoint]
    ) -> str:
        if (
            point.symbol
            and "Scenic Area" in point.symbol
            or re.search(r"\bScenic Area\b|\bPhotos?\b|\b(P)\b", point.name or "", re.I)
        ):
            if not point.symbol:
                point.symbol = "Photos"
            return "P"
        return ""

    @staticmethod
    def _is_restroom(
        point: Union[gpxpy.gpx.GPXWaypoint, gpxpy.gpx.GPXRoutePoint]
    ) -> str:
        if (
            point.symbol
            and "Restroom" in point.symbol
            or re.search(r"\bRestroom\b|\bBreak\b|\b(R)\b", point.name or "", re.I)
        ):
            if not point.symbol:
                point.symbol = "Restroom"
            return "B"
        return ""

    @staticmethod
    def _shaping_point(
        point: Union[gpxpy.gpx.GPXWaypoint, gpxpy.gpx.GPXRoutePoint]
    ) -> bool:
        """:return: True if route point is a shaping/Via point"""
        if not point.name:
            return True
        if point.name.startswith("Via ") or point.name.endswith("(V)"):
            return True
        for extension in point.extensions:
            if "ShapingPoint" in extension.tag:
                return True
        return False
