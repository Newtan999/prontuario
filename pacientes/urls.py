from django.urls import path
from . import views

app_name = 'pacientes' # <- Necessário para usar NAMESPACE no template

urlpatterns = [
    path('', views.listar_pacientes, name='listar_pacientes'),
    path('novo/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('editar/', views.editar_paciente, name='editar_paciente'),
    path('excluir', views.excluir_paciente, name='excluir_paciente'),
]