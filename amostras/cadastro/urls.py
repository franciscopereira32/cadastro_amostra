from django.urls import path
from .views import CampoCreate

urlpatterns = [
    path('cadastro/campo/', CampoCreate.as_view(), name="cadastrar-campo"),
]