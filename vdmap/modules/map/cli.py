from json import load, dump
from werkzeug.security import generate_password_hash

from . import poi


class Cli:
    def __init__(self, map_):
        self.path = map_.path
        self.points = map_.points

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            dump({"points": [po.serialize() for po in self.points]}, f, ensure_ascii=False)

    @staticmethod
    def generate_admin(login, password):
        return generate_password_hash(f"{login}:{password}")

    def make_context(self):
        return {"p": self}
