from django.conf.urls import patterns, url
from shop import views


urlpatterns = patterns('',
    url(r'^$', views.shop, name='shop'),
)
