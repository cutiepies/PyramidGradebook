from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

#from .security import groupfinder

def hello_world(request):
    return Response('Hello World!')

def teacher(request):
    return Response('<body><h3>Welcome to the Teacher Portal</h3></body>')

def login(request):
    print('Incoming request')
    return Response('<body><h1>Welcome to Gradebook!</h1><h3>Please login with your email!<br><button type="button">Login!</button></h3></body>')

def student(request):
    return Response('<body><h3>Welcome to the Student Portal</h3></br><h5>Your classes are displayed below</h5></body>')
if __name__ == '__main__':
    with Configurator() as config:
        #index login config
        config.add_route('login', '/')
        config.add_view(login, route_name='login')
        #student config
        config.add_route('student', '/student')
        config.add_view(student, route_name='student')
        #teacher config
        config.add_route('teacher', '/teacher')
        config.add_view(teacher, route_name='teacher')

        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
