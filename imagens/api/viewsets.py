from rest_framework import viewsets

from imagens.models import ImagensHistorico, FotoPaciente
from imagens.api.serializers import ImagensHistoricoSerializer, FotoPacienteSerializer


class ImagensHistoricoViewSet(viewsets.ModelViewSet):
    queryset = ImagensHistorico.objects.all()
    serializer_class = ImagensHistoricoSerializer


class FotoPacienteViewSet(viewsets.ModelViewSet):
    queryset = FotoPaciente.objects.all()
    serializer_class = FotoPacienteSerializer