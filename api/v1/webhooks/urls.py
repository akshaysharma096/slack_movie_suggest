from django.conf.urls import url

from .views import FacebookView

urlpatterns = [
    url(r'^facebook/$', FacebookView.as_view(), name='facebook'),
]
