from math import ceil
from pprint import pprint

import polyline as polyline
import requests


class RouteCreator:
    def __init__(self):
        self.s = requests.Session()

    def generate_route(self, point1, point2):
        r = self.s.get(
            f"http://router.project-osrm.org/route/v1/foot/{point1[0]},{point1[1]};"
            f"{point2[0]},{point2[1]}")
        if r.status_code != 200:
            return None
        j = r.json()
        route = map(lambda x: list(reversed(x)),
                    polyline.decode(j.get("routes")[0].get("geometry")))
        return list(route), ceil(j.get("routes")[0].get("duration") / 60)
