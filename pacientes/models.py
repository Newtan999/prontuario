from django.db import models

class Pacientes(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.nome