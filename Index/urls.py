from django.conf.urls import patterns, url
from Index import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
)

