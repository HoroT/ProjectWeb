from .poi import Poi, Type


class Point(Poi):
    def __init__(self, params):
        super().load(params)
        self.type = Type.POINT
