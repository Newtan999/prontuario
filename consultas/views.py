from django.shortcuts import render, redirect
from .models import Consulta
from .forms import ConsultaForm

def listar_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas/listar_consultas.html', {'consultas': consultas})


def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultas:listar_consultas')
    else:
        form = ConsultaForm()
    return render(request, 'consultas/form_consulta.html', {'form': form})    