from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.ProductList.as_view(), name='hello'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='detail'),
	url(r'^new$', views.ProductNew.as_view(), name='new'),
	url(r'^edit/(?P<pk>\d+)$', views.ProductEdit.as_view(), name='edit'),
	url(r'^delete/(?P<pk>\d+)$', views.ProductDelete.as_view(), name='delete'),

	url(r'^login$', views.auth_login, name='authentication'),
	url(r'^logout$', auth_views.logout, {'next_page': '/'}, name='logout'),
] 