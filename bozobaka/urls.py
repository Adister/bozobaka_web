from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from bozobaka.views import home
from qrcodes.views import log_order, log_rating, log_new_qr
from users.views import validate_request
 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bozobaka.views.home', name='home'),
    # url(r'^bozobaka/', include('bozobaka.bozobaka.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Homepage
    url(r'^$', home),

    # URL to log user data sent by phone into DB
    url(r'^loguser', validate_request),

    # URL for scanned code logging
    url(r'^code', log_new_qr),

    # URL for logging the rating sent
    url(r'^rating', log_rating),

    # URL for logging the order type event
    url(r'^order', log_order),
)
