from django.db import models
from pacientes.models import Pacientes


class Agendamentos(models.Model):
    id_agendamento = models.AutoField(primary_key=True)
    data_hora = models.DateTimeField(blank=False, null=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    cancelado = models.BooleanField(default=False)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    id_paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE, related_name='agendamentos',
                                    blank=False, null=False)

    def __str__(self):
        return str(self.id_agendamento)

    class Meta:
        managed = True
        db_table = 'agendamentos'
        # Não pode haver um mesmo paciente no mesmo horário
        unique_together = ('data_hora', 'id_paciente')