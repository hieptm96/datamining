from django.conf.urls import url

from . import views
from .controllers import IndexController

urlpatterns = [
  # url /
  url(r'^$', views.index, name='index'),
  # url /test
  url(r'^test', IndexController.index, name='index'),
  url(r'^top-word', IndexController.remove, name='remove'),
]
