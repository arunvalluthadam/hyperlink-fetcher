from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hyperlink_fetcher.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home/$', 'hyperlink.views.home'),
    url(r'^show/$', 'hyperlink.views.show'),

    url(r'^admin/', include(admin.site.urls)),
)
