from django.contrib import admin
from .models import *



@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Hidrometro)
class HidrometroAdmin(admin.ModelAdmin):
    readonly_fields = ['leitura_balanco']
    fields = ['cliente', 'identificacao', 'leitura_balanco']

@admin.register(Leitura)
class LeituraAdmin(admin.ModelAdmin):
    readonly_fields = ['leitura_diferenca']
    fields = ['hidrometro', 'leitura_atual', 'leitura_diferenca']