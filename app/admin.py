from django.contrib import admin

# Register your models here.
from .models import News, Cluster

admin.site.register(News)
admin.site.register(Cluster)
