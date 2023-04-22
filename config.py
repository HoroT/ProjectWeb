import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    HOST = os.environ.get("HOST", "0.0.0.0")
    PORT = int(os.environ.get("PORT", 8000))
    DATABASE = os.environ.get("DATABASE", "sqlite:///db.sqlite")
    DEV = os.environ.get("DEV", False)
    ADMIN_AUTH = os.environ.get("ADMIN_AUTH", "")
