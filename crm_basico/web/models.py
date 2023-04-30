from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.PositiveIntegerField()
    sector = models.CharField(max_length=50, null=True)
    ciudad = models.ForeignKey(Ciudad, models.CASCADE)

    def __str__(self) -> str:
        return(f'{self.calle} {self.numero}, {self.ciudad}')

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.OneToOneField(Direccion, models.CASCADE)
    email = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=12)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return(f'{self.nombre} {self.apellido}')
