from django.db import models

# Create your models here.

class Carausel(models.Model):
    judul       = models.CharField(max_length=200)
    keterangan  = models.CharField(max_length=500) 
    foto        = models.ImageField(upload_to='carausel/')

    def __str__(self):
        return self.judul
