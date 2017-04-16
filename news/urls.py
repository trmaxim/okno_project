from django.conf.urls import url
from .views import ListNews, DetailNews


urlpatterns = [
    url(r'^$', ListNews.as_view(), name='news'),
    url(r'^news/(?P<slug>[-\w]+)/$', DetailNews.as_view(), name='detail'),
    url(r'^category/(?P<slug>[-\w]+)/$', DetailNews.as_view(), name='category'),

]