from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('agenda', include('contact.urls')),
    path('admin/', admin.site.urls),
]
