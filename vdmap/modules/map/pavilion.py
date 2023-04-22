from .poi import Poi, Type


class Pavilion(Poi):
    def __init__(self, params):
        super().load(params)
        self.type = Type.PAVILION
