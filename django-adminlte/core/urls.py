"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
from admin_adminlte import views

urlpatterns = [
    
    # 
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls', namespace='inventario')),
    path('personas/', include('personas.urls', namespace='personas')),
    path('licencias/', include('licencias.urls', namespace='licencias')),
    
    path('', include('home.urls')),
    path('', include('admin_adminlte.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

