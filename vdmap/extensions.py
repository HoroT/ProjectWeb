from flask_login import LoginManager

from config import Config
from vdmap import db
from vdmap.db.models.users import Users
from vdmap.modules.map import map_, rc

config = Config()
d = db.create_session
login = LoginManager()
login.login_view = "index.index"


@login.user_loader
def user_loader(i):
    return d().query(Users).filter(Users.id == int(i)).first()
