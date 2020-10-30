from django.db import models
from django.urls import reverse 
import uuid 
from ckeditor.fields import RichTextField

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    fecha_nac = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['nombre', 'apellido']

    def get_absolute_url(self):
        return reverse('autor-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'

class Genero(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Analisis(models.Model):
    id = models.AutoField(primary_key = True)
    juego = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    genero = models.ManyToManyField(Genero)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    contenido = RichTextField()
    #nota = models.IntegerField()
    #imagen
    #fecha = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.juego

