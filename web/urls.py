#coding:utf-8
__author__ = 'Administrator'
from django.conf.urls import patterns,include,url
from web import views
from django.conf import settings

urlpatterns = [
    url(r'^$',views.index),
    url(r'^SendMsg/$',views.SendMsg),
    url(r'^getChat/$',views.getChat),
    url(r'^getChat2/$',views.getChat2),
    url(r'^addLike/$',views.addLike),
    url(r'^getReply/$',views.getReply),
    url(r'^submitReply/$',views.submitReply),
    url(r'^blog/$',views.blog),
    url(r'^blog/(\d*)/$',views.blog),
    url(r'^account/$',views.Account),
    url(r'^SignIn/$',views.SignIn),
    url(r'^SignOut/$',views.SignOut),
    url(r'^newsdetails/(?P<pk>\d+)/$',views.NewsDetalis),
    url(r'^GetContent/$',views.GetContent),
    url(r'^about/$',views.about),
    url(r'^SearchNews/',views.SearchNews),
    url(r'^market/$', views.Market),
    url(r'^upload/$', views.upload),
    url(r'^goodslist/$', views.GoodsList),
    url(r'^sales/$', views.Sales),
    url(r'^buyer/$', views.Buyer),
    url(r'^GoodsDetails/$', views.GoodsDetails),
    url(r'^SearchGoods/$', views.SearchGoods),
    url(r'^payment/(?P<way>[^/]+)/$', views.payment),
    url(r'^management/$', views.Management),
]