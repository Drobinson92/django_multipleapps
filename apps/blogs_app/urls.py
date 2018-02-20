from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^blogs$', views.index),
    url(r'^blogs/new$', views.new),
    url(r'^blogs/create$', views.create),
    url(r'^blogs/(?P<number>\w+)$', views.show),
    url(r'^blogs/(?P<number>\w+)/edit$', views.edit),
    url(r'^blogs/(?P<number>\w+)/delete$', views.destroy),
    url(r'^$', views.index)
]