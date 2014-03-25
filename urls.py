from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rapsite.views.home', name='home'),
    # url(r'^rapsite/', include('rapsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^$', 'pages.views.MainHomePage'),
    (r'^albums/$', 'album.views.AlbumsAll'),
    (r'^albums/(?P<albumslug>.*)/$', 'album.views.SpecificAlbum'),
    (r'^rappers/(?P<rapperslug>.*)/$', 'album.views.SpecificRapper'),
    (r'^register/$', 'siteusers.views.SiteUserRegistration'),
    (r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'), 
    (r'^resetpassword/$', 'django.contrib.auth.views.password_reset'), 
    (r'^reset/(?<uidb36>[0-9A-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
    (r'^login/$', 'siteusers.views.LoginRequest'),
    ('^logout/$', 'siteusers.views.LogoutRequest'),
)
