from django.db import models
from pacientes.models import Pacientes

class Consulta(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.PROTECT)
    data = models.DateTimeField()
    motivo = models.TextField(blank=True)
    evolucao = models.TextField()
    prescricao = models.TextField()

    def __str__(self):
        return f'Consulta de {self.paciente.nome} em {self.data.strftime("%d%m%y %H:%M")}'