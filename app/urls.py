from django.conf.urls import url

from . import views
from .controllers import IndexController

urlpatterns = [
  # url /
  url(r'^$', views.index, name='index'),
  # url /test
  url(r'^clustering', IndexController.clustering, name='clustering'),
  url(r'^top-word', IndexController.remove, name='remove'),
  url(r'^process-raw-data', IndexController.process_raw_data, name='process_raw_data'),
  url(r'^ranking', IndexController.ranking, name='ranking'),
]
