from django.conf.urls import url

from . import views

app_name = 'valley_green_landscape'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^reviews/$', views.reviews, name='reviews'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
]