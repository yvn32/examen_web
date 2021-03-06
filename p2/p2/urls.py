"""p2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
    path('registro/', views.registro, name="registro"),
    path('login/', views.login, name="login"),
    path('salir/', views.salir, name="salir"),
    path('mantenedor/', views.mantenedor, name="mantenedor"),
    path('mantenedorUsuarios/', views.mantenedorUsuarios, name="mantenedorUsuarios"),
    path('eliminarUsuario/<id>', views.eliminarUsuario),
    path('editarUsuario/<id>', views.editarUsuario),
    path('mantenedorProductos/', views.mantenedorProductos, name="mantenedorProductos"),
    path('eliminarProducto/<id>', views.eliminarProducto, name="eliminarProducto"),
    path('ingresarProductos/', views.ingresarProductos, name="ingresarProductos"),
    path('editarProductos/<pk>', views.editarProductos ,name="editarProductos"),
    path('seguimiento/', views.seguimiento, name="seguimiento"),
    path('donacion/', views.donacion, name="donacion"),
    path('carritoCompra/', views.carritoCompra, name="carritoCompra"),
    path('productos/', views.productos, name="productos"),
    path('plantilla/', views.plantilla, name="plantilla"),
]

