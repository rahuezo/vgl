from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views

app_name = 'valley_green_landscape'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^services/$', views.services, name='services'),
    url(r'^reviews/$', views.reviews, name='reviews'),
    url(r'^review_submission/$', views.review_submission, name='review_submission'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_review/$', views.add_review, name='add_review'),
    url(r'^added_review/$', views.add_review, name='add_review'),
    url(r'^send_email/$', views.send_email, name='send_email'),
]
