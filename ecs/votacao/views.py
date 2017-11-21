from django.shortcuts import render

from votacao.models import *
# import para API
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from votacao.serializers import *



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EleitorViewSet(viewsets.ModelViewSet):
  queryset = Eleitor.objects.all()
  serializer_class = EleitorSerializer

class CandidatoViewSet(viewsets.ModelViewSet):
  queryset = Candidato.objects.all()
  serializer_class = CandidatoSerializer

class TokenViewSet(viewsets.ModelViewSet):
  queryset = Token.objects.all()
  serializer_class = TokenSerializer

class VotarViewSet(viewsets.ModelViewSet):
  queryset = Votar.objects.all()
  serializer_class = VotarSerializer

class VagaViewSet(viewsets.ModelViewSet):
  queryset = Vaga.objects.all()
  serializer_class = VagaSerializer


# Create your views here.
