from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def Hello_World(request):
    print('Incoming request')
    return Response('<body><h1>My First Pyramid Web Page</h1></body>')


if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/')
    config.add_view(Hello_World, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
