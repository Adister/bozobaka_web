from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bozobaka.views.home', name='home'),
    # url(r'^bozobaka/', include('bozobaka.bozobaka.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Homepage
    url(r'^$', 'bozobaka.views.home', name='home'),

    # URL to log user data sent by phone into DB
    url(r'^loguser/', 'users.views.validate_request'),

    # URL for scanned code logging
    url(r'^code', 'qrcodes.views.log_new_qr'),
)
