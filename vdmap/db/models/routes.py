import json

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vdmap.db.models.base import Base


class Routes(Base):
    __tablename__ = "routes"

    id: Mapped[int] = mapped_column(primary_key=True)
    route: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["Users"] = relationship(backref="routes")

    def set_route(self, name, p1, p2):
        self.__setattr__("route", json.dumps({"name": name, "p1": p1, "p2": p2}, ensure_ascii=False))

    def get_route(self):
        r = json.loads(self.route)
        r["name"] = r["name"].replace("->", "⇒")
        return r

    def __repr__(self):
        return f"Route({json.loads(self.route)};{self.user_id})"
