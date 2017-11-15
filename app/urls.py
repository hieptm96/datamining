from django.conf.urls import url

from . import views
from .controllers import testController

urlpatterns = [
  # url /
  url(r'^$', views.index, name='index'),
  # url /test
  url(r'^test', testController.index, name='index'),
]
