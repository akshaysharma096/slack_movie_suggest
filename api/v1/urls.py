from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import get_movie

urlpatterns = [
    url(r'^movies/$', get_movie, name='get-movie'),
    url(r'^webhooks/', include('api.v1.webhooks.urls', namespace='v1-webhooks')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
