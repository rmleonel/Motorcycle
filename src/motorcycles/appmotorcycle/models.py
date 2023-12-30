from django.db import models

class Luxury(models.Model):
    marca = models.CharField(max_length = 20)
    modelo = models.CharField(max_length = 20)
    año = models.IntegerField()

    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.año}"

class Medium(models.Model):
    marca = models.CharField(max_length = 20)
    modelo = models.CharField(max_length = 20)
    año = models.IntegerField()

    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.año}"

class Economy(models.Model):
    marca = models.CharField(max_length = 20)
    modelo = models.CharField(max_length = 20)
    año = models.IntegerField()
    
    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.año}"
