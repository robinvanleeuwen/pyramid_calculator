from wsgiref.simple_server import make_server
from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('views')
        config.add_route("calc", "/calc")
        config.scan()
    return config.make_wsgi_app()

