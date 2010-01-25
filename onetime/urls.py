from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

from onetime.views import cleanup, login

urlpatterns = patterns(''
    (r'^cleanup/$', cleanup),
    (r'^(?P<key>[a-z0-9+])$', login), 
    (r'^$', redirect_to, {'url': None}),
)

