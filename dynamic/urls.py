from django.conf.urls import patterns, include, url

from dynamic import views

urlpatterns = patterns('',

    # http://127.0.0.1:8000/
    url(r'^$', views.index, name='index'),
    
    # http://127.0.0.1:8000/eightball
    url(r'^eightball$', views.question, name='question'),
    # http://127.0.0.1:8000/magic
    url(r'^magic$', views.magic, name='magic'),
    
    
)
