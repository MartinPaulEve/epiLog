'''
    epiLog: an object annotation system
    Copyright 2012 Martin Paul Eve

    This file is part of epiLog.

    epiLog is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    epiLog is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with epiLog. If not, see <http://www.gnu.org/licenses/>.

'''

from django.conf.urls.defaults import *
from epiLog import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from userprofile.urls import en
from django_openid_auth import urls as openid_urls

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'epiLog.views.homepage'),
    (r'^logout/$', 'epiLog.views.logout'),
    
    (r'^accounts/', include('userprofile.urls')),
    
    (r'^openid/', include(openid_urls)),
    
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    from django.views.static import serve
    _media_url = settings.MEDIA_URL
    
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]
        urlpatterns += patterns('',
                                (r'^%s(?P<path>.*)$' % _media_url,
                                 serve,
                                 {'document_root': settings.MEDIA_ROOT}))
        del(_media_url, serve)

