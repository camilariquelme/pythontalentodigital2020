from django.urls import path     
from . import views
urlpatterns = [
    path('libros', views.index),
    path('crear', views.create),
    path('autores', views.index_uno),
    path('info_libros/<int:number>', views.info_libros),
    path('info_libros/agregar_autor/<int:number>',views.agregar_autor),
    path('',views.home),
    path('created', views.created),
    path('info_autor/<int:number>', views.info_autor),
    path('info_autor/agregar_libro/<int:number>',views.agregar_libro),

]