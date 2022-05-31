from rest_framework import serializers

from imagens.models import ImagensHistorico, FotoPaciente


class ImagensHistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagensHistorico
        fields = '__all__'


class FotoPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoPaciente
        fields = '__all__'