from django import path
from . import views

urlpatterns = [
    path('novo/', views_cadastrar_paciente, name='cadastrar_paciente')
]