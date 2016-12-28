from pyramid.view import view_config
from pyramid.response import Response
import logging
log = logging.getLogger(__name__)


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'Welcome to our first web page'}

@view_config(route_name='home', renderer='templates/login.pt')
def my_view(request):
    return {}
