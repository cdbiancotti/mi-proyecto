from django.db import models

class Mesa(models.Model):
    material = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    cant_patas = models.IntegerField()