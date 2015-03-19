from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^basicview/', include('article.urls')),
	url(r'^auth/', include('loginsys.urls')),
	url(r'^', include('article.urls')),
	
)
