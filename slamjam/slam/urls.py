from django.conf.urls import patterns, url
from slam import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
    url(r'^about/$',views.about,name='about'),
    url(r'^signup/$', views.signup, name='signup'),
)
