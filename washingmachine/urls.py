from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^order$', views.order, name='order'),
    url(r'^status$', views.status, name='status'),
    url(r'^wm_order$', views.wm_order, name='wm_order'),
    url(r'^query$', views.query, name='query')
]