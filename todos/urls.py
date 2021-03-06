from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details),#the (?P<id>\w{0}),50 is needed to accept an ID parameter
    url(r'^add', views.add, name='add')
]
