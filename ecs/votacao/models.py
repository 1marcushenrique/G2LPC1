from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Eleitor(models.Model):
    nome = models.CharField('Nome ', max_length=200)
    cpf = models.CharField('CPF ', max_length=200)
    #usuario=models.ForeignKey(User,  null=True, blank=False)



    def __str__(self):
        return str(self.nome)

class Vaga(models.Model):

    nome = models.CharField('Vaga: ', max_length=50)

    def __str__(self):
        return 'Vaga: '+str(self.nome)

class Candidato(models.Model):

    nome = models.OneToOneField(Eleitor, related_name='Nome', null=True, blank=False)
    partido = models.CharField('Partido: ', max_length=10)
    vaga = models.ForeignKey(Vaga, related_name='Nome', null=True, blank=False)

    def __str__(self):
        return 'Candidato: '+str(self.nome) + ' '+str(self.vaga)




class Token(models.Model):

    numero = models.CharField('Numero: ', max_length=10)

    def __str__(self):
        return 'Token: '+str(self.numero)


class Votar(models.Model):
    eleitor = models.OneToOneField(Eleitor, related_name='Nome_Eleitor', null=True, blank=False)
    candidato = models.OneToOneField(Candidato, related_name='Nome_Candidato', null=True, blank=True)
    token = models.OneToOneField(Token)
    branco = models.BooleanField()
    voto = models.BooleanField(default=1)

    def __str__(self):
        return 'Eleitor: '+str(self.eleitor) + ' '+str(self.token)

# Create your models here.
