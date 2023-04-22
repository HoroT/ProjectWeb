from sqlalchemy import create_engine
import config
from .models import base

engine = create_engine(config.Config().DATABASE)
base.Base.metadata.create_all(engine)
