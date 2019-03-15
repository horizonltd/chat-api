
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #This registered the hub url.py here
    path('api/hub/', include('hub.urls')),
]
