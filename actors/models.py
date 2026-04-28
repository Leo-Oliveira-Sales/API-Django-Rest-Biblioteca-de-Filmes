from django.db import models


NATIONALITY_CHOICES = (
    ("Brazil", "Brasileira"),
    ("USA", "Estados Unidos"),
    ("Canada", "Canadense"),
    ("France", "Francesa"),
    ("Germany", "Alemã"),
    ("Spain", "Espanhola"),
    ("UK", "Reino Unido"),
    ("Italy", "Italiana"),
    ("Japan", "Japonesa"),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
