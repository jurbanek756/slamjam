from django.conf.urls import patterns, url
from slam import views

urlpatterns = patterns('',
                       url(r'^$', views.home, name='home'),
                       )