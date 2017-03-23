from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.RestaurantesView.as_view(), name="list"), 
	url(r'^detalle/(?P<id>[0-9]+)/$', views.DetailRestView.as_view(), name='detail')
]