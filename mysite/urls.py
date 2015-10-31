from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()

from mysite.views import im_here, math, meta, welcome, set_ck, get_ck, use_session, index#, login, logout
# from mysite.views import math
from restaurants.views import menu, list_restaurants, comment
# from mysite.views import meta
# from mysite.views import welcome

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/$', im_here),
    # url(r'^(\d{1,5})/math/(\d{1,5})/$', math),
    url(r'^(?P<b>[0-9]{1,5})/math/(?P<a>\d{1,5})/$', math),
    url(r'^menu/$', menu),
    #url(r'^menu/(\d{1,5})/$', menu),
    url(r'^meta/$', meta),
    url(r'^comment/(\d{1,5})/$', comment),
    url(r'^welcome/$', welcome),
    url(r'^restaurants_list/$', list_restaurants),
    url(r'^setcookies/$', set_ck),
    url(r'^getcookies/$', get_ck),
    url(r'^usesessions/$', use_session),
    url(r'^accounts/login/$', login), #{'template_name': 'login.html'}),
    url(r'^accounts/logout/$', logout),
    url(r'^index/$', index),
    #url(r'^accounts/profile/$', index),
)
