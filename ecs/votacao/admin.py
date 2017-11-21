from django.contrib import admin
from votacao.models import *

admin.site.register(Eleitor)
admin.site.register(Candidato)
admin.site.register(Token)
admin.site.register(Votar)
admin.site.register(Vaga)

# Register your models here.
