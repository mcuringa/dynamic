from django.conf.urls import patterns, include, url

from dynamic import views, review_views, user_views

urlpatterns = patterns('',

    #--------------------------------------------- apps stuff
    url(r'^$', views.app_list),
    url(r'^add_app$', views.app_form), 
    url(r'^app/(?P<pk>[0-9]?)/edit[/]$', views.app_form), 
    url(r'^save_app$', views.save_app),
    url(r'^app/([0-9]?)/del[/]$', views.del_app),
    url(r'^app/([0-9]?)[/]$', views.app_detail),
    
    #--------------------------------------------- ratings & reviews
    url(r'^rate/([0-9]?)/([0-9]?)[/]$', review_views.rate_app),
    url(r'^review/([0-9]?)[/]$', review_views.review),
    url(r'^save_review$', review_views.save_review),
    
    #--------------------------------------------- user login
    url(r'^login$', user_views.user_login),
    url(r'^logout$', user_views.user_logout),
    url(r'^login-sorry$', user_views.login_error),
    url(r'^register$', user_views.register),

)
