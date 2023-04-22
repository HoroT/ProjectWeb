from vdmap.db import db
from sqlalchemy.orm import Session

from vdmap.db.db import engine


def create_session() -> Session:
    return Session(engine)
