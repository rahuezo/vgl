from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views

app_name = 'valley_green_landscape'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^reviews/$', views.reviews, name='reviews'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    # url(r'^signup/$', views.signup, name='signup'),
    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),


]