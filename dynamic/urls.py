from django.conf.urls import patterns, include, url

from dynamic import views, review_views, user_views

urlpatterns = patterns('',

    #--------------------------------------------- apps stuff
                                                               # Examples
                                                               #------------------------------------
    url(r'^$', views.app_list),                                # http://127.0.0.1:8000/
    url(r'^add_app$', views.app_form),                         # http://127.0.0.1:8000/add_app
    url(r'^app/([0-9]?)[/]$', views.app_detail),               # http://127.0.0.1:8000/app/12
    url(r'^app/(?P<pk>[0-9]?)/edit[/]$', views.app_form),      # http://127.0.0.1:8000/app/12/edit
    url(r'^app/([0-9]?)/del[/]$', views.del_app),              # http://127.0.0.1:8000/app/12/del
    url(r'^save_app$', views.save_app),                        # http://127.0.0.1:8000/save_app
    
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
