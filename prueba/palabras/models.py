from django.db import models

class Frase(models.Model):
    palabra = models.CharField(max_length=50, unique=True)
    frase = models.CharField(max_length=200)