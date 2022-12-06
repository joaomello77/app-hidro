from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models import Sum
from django.core.exceptions import ValidationError


class Cliente(models.Model):
    nome = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome

class Hidrometro(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=CASCADE)
    identificacao = models.CharField(max_length=20, unique=True)

    @property
    def leitura_balanco(self): 
        return str(Leitura.objects.filter(hidrometro=self.id).aggregate(total=Sum('leitura_atual'))['total'])
    
    def __str__(self):
        return self.identificacao
        

class Leitura(models.Model):
    hidrometro = models.ForeignKey(Hidrometro, on_delete=CASCADE)
    leitura_atual = models.IntegerField()
    leitura_diferenca = models.IntegerField(null=True, blank=True, editable=False)

    def clean(self):
        leitura_anterior = int(str(Leitura.objects.filter(hidrometro=self.hidrometro).latest('leitura_atual')))
        
        if self.leitura_atual <= leitura_anterior:
            raise ValidationError('Leitura atual menor que a anterior')

        self.leitura_diferenca = self.leitura_atual - leitura_anterior
        
    def __str__(self):
        return str(self.leitura_atual)



    


