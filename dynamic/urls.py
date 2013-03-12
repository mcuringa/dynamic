from django.conf.urls import patterns, include, url

from dynamic import views

urlpatterns = patterns('',

    # http://127.0.0.1:8000/
    url(r'^$', views.index, name='index'),

    url(r'^add_app$', views.app_form),
    url(r'^app/(?P<slug>.+?)/edit[/]$', views.app_form),
    url(r'^save_app$', views.save_app),
    url(r'^app/(.+?)/del[/]$', views.del_app),
    url(r'^app/(.+?)[/]$', views.app_detail),

)
