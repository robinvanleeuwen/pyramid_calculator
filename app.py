from wsgiref.simple_server import make_server

from pyramid.config import Configurator

if __name__ == '__main__':
    print("Starting APP")
    with Configurator() as config:
        config.add_route("calc", "/calc")
        config.scan("views")
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
