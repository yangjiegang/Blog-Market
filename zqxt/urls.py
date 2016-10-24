#coding:utf-8
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from DjangoUeditor import urls as DjangoUeditor_urls
#from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}), #static配置
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}), #media配置
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^web/', include('web.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
# urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
# urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )