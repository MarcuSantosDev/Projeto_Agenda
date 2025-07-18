from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings # para importar media url e static url

urlpatterns = [
    path('agenda', include('contact.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
