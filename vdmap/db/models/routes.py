import json

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from vdmap.db.models.base import Base


class Routes(Base):
    __tablename__ = "routes"


    id = Column( Integer, primary_key=True )
    route = Column( String )
    user_id = Column( ForeignKey( 'users.id' ) )
    user = relationship( 'Users', backref="routes" ) 
    
    def set_route(self, name, p1, p2):
        self.__setattr__("route", json.dumps({"name": name, "p1": p1, "p2": p2}, ensure_ascii=False))

    def get_route(self):
        r = json.loads(self.route)
        r["name"] = r["name"].replace("->", "⇒")
        return r

    def __repr__(self):
        return f"Route({json.loads(self.route)};{self.user_id})"

print( Routes )

