from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from Rainmaker import views


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^shop/', include('shop.urls')),
    url(r'^$', views.index, name='index'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
