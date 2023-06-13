from django.db import models

# Create your models here.

class mahasiswaModels(models.Model):
    Nim   = models.CharField(max_length=50)
    Nama   = models.CharField(max_length=50)
    Kelamin  = models.CharField(max_length=50)
    Alamat    = models.CharField(max_length=50)

def __str__(self):
        return "{}".format(self.nim)