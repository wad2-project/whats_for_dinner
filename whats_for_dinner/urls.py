from django.conf.urls import url
from whats_for_dinner import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^result/', views.result, name='result'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.log_in, name='login'),
	url(r'^logout/$', views.log_out, name='logout'),
	url(r'^myfavourites/$', views.favourites, name='favourites'),
	url(r'^myfavourites/modify$', views.modify, name='modify'),
]