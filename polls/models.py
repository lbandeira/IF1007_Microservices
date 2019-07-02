from django.db import models
from django.utils import timezone

# Create your models here.
class usuario(models.Model):
   	
	usuario = models.CharField(max_length=254)
	nome_usuario = models.CharField(max_length=240)	
	email_usuario = models.EmailField(max_length=254)

	def __str__(self):
		return self.nome_usuario
