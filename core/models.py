from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome',max_length=100)
    preco = models.DecimalField('Preço', decimal_places= 2, max_digits=9)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.nome
