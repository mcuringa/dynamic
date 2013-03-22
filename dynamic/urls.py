from django.conf.urls import patterns, include, url

from dynamic import views

urlpatterns = patterns('',

    # http://127.0.0.1:8000/
    url(r'^$', views.index, name='index'),
    url(r'^add_app$', views.app_form), # "/add_app"
    url(r'^app/(?P<pk>[0-9]?)/edit[/]$', views.app_form), # "/app/22/edit"
    url(r'^save_app$', views.save_app),
    url(r'^app/([0-9]?)/del[/]$', views.del_app),
    url(r'^app/([0-9]?)[/]$', views.app_detail),
    url(r'^rate/([0-9]?)/([0-9]?)[/]$', views.rate_app),
    
    
    #--------------------------------------------- user login
    url(r'^login$', views.user_login),
    url(r'^login-sorry$', views.login_error),
    url(r'^register$', views.register),


)
