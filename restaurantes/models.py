from django.db import models

# Create your models here.

class Restaurante(models.Model):

	nombre = models.CharField(max_length=100)
	horario = models.DateTimeField(auto_now_add=False, db_index=True)
	dueño = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to="restaurantesimgs")
	direccion = models.TextField()

	def __str__(self):
		return self.nombre
