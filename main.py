from vdmap.db.models import users, routes
from vdmap import create_app, db, config
from vdmap.modules.map import cli

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {**{"db": db, "Users": users.Users, "Routes": routes.Routes}, **cli.make_context()}


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)
