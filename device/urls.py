from django.conf.urls import patterns, url
from device import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^_nexusinfo/', views._nexusinfo, name='_nexusinfo'),
  url(r'^authenticate/', views.authenticate, name='authenticate'),
  url(r'^(?P<consumer>[\w@\.]{3,50})/$', views.subscriberDevices, name='subscriberDevices'),
)
