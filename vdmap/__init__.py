from flask import Flask

from vdmap.extensions import config, d, login


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    login.init_app(app)
    from vdmap.views.index import index_bp
    app.register_blueprint(index_bp)
    from vdmap.views.auth import auth_bp
    app.register_blueprint(auth_bp)
    from vdmap.views.map import map_bp
    app.register_blueprint(map_bp)
    if config.DEV:
        from jinja2 import Environment, PackageLoader, select_autoescape
        app.jinja_env = Environment(
            loader=PackageLoader('vdmap', 'templates'),
            autoescape=select_autoescape(['html', 'xml']),
            cache_size=0
            )
    return app
