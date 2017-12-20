from django.conf.urls import include, url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.post_list, name='blog'),

    url(r'^home/$', views.home, name='home'),
  # url(r'^login/$', auth_views.login, name='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
  # url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logged_out.html'}, name='logout'),
  #	url(r'^admin/', admin.site.urls),
]