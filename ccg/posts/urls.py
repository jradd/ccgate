from django.conf.urls import patterns, url, include

from rest_framework.urlpatterns import format_suffix_patterns

from posts import views


urlpatterns = patterns('',
    url(r'^$', views.PostList.as_view(), name='post-list'),
    url(r'^(?P<pk>\d+)/$', views.PostDetail.as_view(), name='post-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
