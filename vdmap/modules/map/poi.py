from enum import IntEnum
from typing import List


class Type(IntEnum):
    POINT = 1
    PAVILION = 2
    MONUMENT = 3


class Poi:
    name: str
    description: str
    coordinates: List[float]
    type: Type

    def load(self, params):
        self.name = params.get("name")
        self.description = params.get("description")
        self.coordinates = params.get("coordinates")

    def serialize(self):
        return {
            "type": self.type,
            "name": self.name,
            "description": self.description,
            "coordinates": self.coordinates
            }

    def __repr__(self):
        return f"{self.type}, {self.name}, {self.coordinates}"
