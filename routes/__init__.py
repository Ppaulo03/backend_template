from .home import HomeRoute


def register_routes(app):
    HomeRoute(app)
    # Include other routes here as needed
