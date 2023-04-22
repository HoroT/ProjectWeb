from .poi import Poi, Type


class Monument(Poi):
    def __init__(self, params):
        super().load(params)
        self.type = Type.MONUMENT
