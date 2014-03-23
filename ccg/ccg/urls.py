from django.conf.urls import patterns, include, url

from api import views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^shop/', include('shopping.urls', namespace='shopping')),
    url(r'^admin/', include(admin.site.urls)),
    #index
    url(r'^$', 'posts.views.home', name="home"),
    #posts
    (r'^posts/', include('posts.urls')),
    #tags
    (r'^tags/', include('tags.urls')),
    )
