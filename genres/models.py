from django.db import models


# Banco de Dados
class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
