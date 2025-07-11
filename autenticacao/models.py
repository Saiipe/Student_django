from django.db import models


class Pessoa(models.Model):
    nome: models.CharField = models.CharField(max_length=50)
    email: models.EmailField = models.EmailField()
    senha: models.CharField = models.CharField(max_length=50)
