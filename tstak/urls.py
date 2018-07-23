"""tstak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#from django.urls import path
from django.conf.urls import url
from mensajeria import views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^servicios', views.servicio, name='servicio'),
    url(r'^sesion', views.nuevo_usuario, name='sesion'),
    url(r'^ingresar', views.ingresar, name='ingresar'),
    url(r'^privado', views.privado, name='privado'),
    url(r'^cerrar', views.cerrar, name='cerrar'),
    url(r'^archivos', views.files, name='archivos'),
    url(r'^media/excel/', views.archi, name='files'),
    url(r'^editar-perfil', views.edit_perejil, name='perejil'),
    url(r'^mensajeria', views.mensajeria, name='mensajeria'),
]