from django.shortcuts import render, redirect
from .forms import PacienteForm
from .models import Pacientes

def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pacientes:listar_pacientes') # incluído o namespace 'pacientes'
    else:
        form = PacienteForm()
    return render(request, 'pacientes/form_paciente.html', {'form': form})

def listar_pacientes(request): #nome "listar_pacientes" padronizado
    pacientes = Pacientes.objects.all()
    return render(request, 'pacientes/listar_pacientes.html', {'pacientes': pacientes})

def editar_pacientes(request):
    