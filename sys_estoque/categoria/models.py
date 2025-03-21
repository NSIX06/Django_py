from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.nome}, {self.descricao}"