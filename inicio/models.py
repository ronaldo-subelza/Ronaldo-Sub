from django.db import models



class Ropa(models.Model):
    prenda = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    talla = models.IntegerField()
    def __str__(self):
        return f'{self.prenda} {self.marca}'