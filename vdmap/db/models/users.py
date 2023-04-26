from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from vdmap.db.models.base import Base


class Users(Base, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    def set_password(self, password):
        self.__setattr__("password", generate_password_hash(password))

    def check_password(self, password):
        return check_password_hash(self.__getattribute__("password"), password)

    def get_routes(self):
        routes = self.__getattribute__("routes")
        return [r.get_route() for r in routes]

    def __repr__(self):
        return f"User(id={self.id},email={self.email})"
