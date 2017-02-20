from django.conf.urls import url

from .views import get_movie

urlpatterns = [
    url(r'^movie/$', get_movie, name='get-movie'),
]
