from django.conf.urls import url

from . import views

urlpatterns = [
  # url /
  url(r'^$', views.index, name='index'),
  # url /test
  url(r'^test', views.test, name='test'),
]
