"""clinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

from pacientes.api.viewsets import PacientesViewSet
from agendamentos.api.viewsets import AgendamentosViewSet
from historicos.api.viewsets import HistoricosViewSet
from imagens.api.viewsets import ImagensHistoricoViewSet, FotoPacienteViewSet

router = routers.DefaultRouter()
router.register(r'pacientes', PacientesViewSet)
router.register(r'agendamentos', AgendamentosViewSet)
router.register(r'historicos', HistoricosViewSet)
router.register(r'imagens_historicos', ImagensHistoricoViewSet)
router.register(r'foto_pacientes', FotoPacienteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

