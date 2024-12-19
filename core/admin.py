from django.contrib import admin

from django.contrib import admin
from .models import Aluno, Plano, Treino, Contrato,FormaDePagamento

# Registro básico
admin.site.register(Aluno)
admin.site.register(Plano)
admin.site.register(Treino)
admin.site.register(Contrato)
admin.site.register(FormaDePagamento)

