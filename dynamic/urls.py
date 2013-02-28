from django.conf.urls import patterns, include, url

from dynamic import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^eightball$', views.question, name='question'),
    url(r'^magic$', views.magic, name='magic'),
)
