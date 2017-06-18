from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^valley_green_landscape/', include('valley_green_landscape.urls')),
    url(r'^admin/', admin.site.urls),
]