from .home import HomeRoute


def register_routes(app):
    HomeRoute(app)
