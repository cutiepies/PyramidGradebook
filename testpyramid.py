from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

#from .security import groupfinder

def hello_world(request):
    return Response('Hello World!')

def login(request):
    print('Incoming request')
    return Response('<body><h1>Welcome to Gradebook!</h1><h3>Please login with your email!<br><button type="button">Login!</button></h3></body>')

def student(request):
    return Response('<body></body>')
if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('login', '/')
        config.add_view(login, route_name='login')
        config.add_route('hello', '/student')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()