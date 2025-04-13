from django.urls import path
from . import views

app_name = 'consultas'

urlpatterns = [
    path('nova/', views.criar_consulta, name='criar_consulta'),
    path('', views.listar_consultas, name = 'listar_consultas'),
]