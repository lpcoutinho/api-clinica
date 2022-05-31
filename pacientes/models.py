from django.db import models


def foto_paciente(instance,filename):
    return '/'.join(['foto_pacientes', str(instance.id), filename])


class Pacientes(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    data_nas = models.DateTimeField(blank=True, null=True)
    rg = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    num_endereco = models.IntegerField(blank=True, null=True)
    bairro_endereco = models.CharField(max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(blank=True, null=True, upload_to=foto_paciente)

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        db_table = 'pacientes'
