from django.shortcuts import render, redirect
from .forms import PacienteForm

def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes') # -> CONSTRUIR! - 14/04
        else:
            form = PacienteForm()
        return render(request, 'form_paciente.html', {'form': form})