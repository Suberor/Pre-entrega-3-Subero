from django.db import models

    
class Spells(models.Model):

    nombre = models.CharField(max_length=30)
    nivel = models.IntegerField()
    escuela = models.CharField(max_length=30)

class Monsters(models.Model):

    nombre = models.CharField(max_length=30)
    nivel_desafio = models.IntegerField()
    terreno = models.CharField(max_length=30)

class Weapons(models.Model):

    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    versatil = models.BooleanField()







