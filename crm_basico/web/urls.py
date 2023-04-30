from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar sesion'),
    path('registro-usuario/', views.registro_usuario, name='registro usuario'),

]
