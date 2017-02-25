from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import get_movie

urlpatterns = [
    url(r'^movies/$', get_movie, name='get-movie'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
