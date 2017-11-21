from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from votacao.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('url', 'username', 'email', 'is_staff')


class EleitorSerializer(serializers.HyperlinkedModelSerializer):
    usuario=UserSerializer(many=False)
    class Meta:
        model = Eleitor
        fields = ('nome', 'cpf', 'usuario')


    def create(self, dados):
      dados_user = dados.pop('usuario')
      u=User.objects.create(**dados_user)
      p=Eleitor.objects.create(usuario=u, **dados)
      return p


class CandidatoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Candidato
        fields = ('candidato', 'partido', 'vaga')




class VagaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Vaga
        fields = ('nome')



class TokenSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Token
        fields = ('numero')



class VotarSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Votar
        fields = ('eleitor', 'token')
