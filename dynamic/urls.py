from django.conf.urls import patterns, include, url

from dynamic import views

urlpatterns = patterns('',

    # http://127.0.0.1:8000/
    url(r'^$', views.index, name='index'),
    
    url(r'^new_app$', views.app_form),
    url(r'^save_app$', views.save_app),
    url(r'^app/(.*)[/]$', views.detail),
    url(r'^app/(.*?)/del[/]$', views.delete),
    
    
    
    
)
