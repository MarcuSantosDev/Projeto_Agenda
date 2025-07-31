from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings # para importar media url e static url
from contact import views   
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('agenda/', include('contact.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), # URL LOGIN
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'), # URL LOGOUT
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
