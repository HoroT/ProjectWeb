from typing import List, Optional, Union
from os import path as p
from json import load

from .poi import Poi, Type
from .pavilion import Pavilion
from .point import Point


class Map:
    path = p.join(p.dirname(p.abspath(__file__)), "data/points.json")

    def __init__(self):
        self.points: List[Poi] = []
        self.center: Optional[Point] = None
        self.load_points()

    def load_points(self):
        with open(self.path, "r", encoding="utf-8") as f:
            points = load(f)
        if points.get("points", None) is None:
            return
        for point in points.get("points"):
            if point.get("type") == Type.PAVILION:
                self.points.append(Pavilion(point))
            if point.get("type") == Type.POINT:
                o = Point(point)
                if o.name == "center":
                    self.center = o
                self.points.append(o)

    def get_points(self, serialized=True) -> Union[List[Poi], List[dict]]:
        if serialized:
            return self.serialized(self.points)
        return self.points

    # noinspection PyTypeChecker
    def get_pavilions(self, serialized=True) -> List[Union[Pavilion, dict]]:
        r: List[Pavilion] = list(filter(lambda x: isinstance(x, Pavilion), self.points))
        if serialized:
            return self.serialized(r)
        return r

    @staticmethod
    def serialized(points: List[Poi]) -> List[dict]:
        return [po.serialize() for po in points]
