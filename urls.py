from django.conf.urls.defaults import patterns, include, url
from django.conf import settings 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from paradise.views import home, contact, coming_soon
from bikes.views import bike_display

from shop import urls as shop_urls


urlpatterns = patterns('',
    url(r'^$',home, name='home'),
    url(r'^bikes/(?P<slug>[\-\d\w]+)/$',  bike_display, name="bike-display"),
    #url(r'^shop/', include(shop_urls), name='shop'),
    url(r'^store/', coming_soon, name='store'),
    url(r'^bikes/', coming_soon, name='bikes'),
    url(r'^blog/', coming_soon, name='blog'),
    url(r'^about/', coming_soon, name='about'),



    url(r'^contact/', contact, name="contact"),
    # Examples:
    # url(r'^$', 'paradise.views.home', name='home'),
    # url(r'^paradise/', include('paradise.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# flat pages
urlpatterns+= patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
)
