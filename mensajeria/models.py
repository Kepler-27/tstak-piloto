from django.db import models
from django.utils import timezone


class FilesExcel(models.Model):
	filename = models.CharField(max_length=100)
	docfile = models.FileField(upload_to='excel/')
	user_iden = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	fecha_subida = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.filename

class FotoPerfil(models.Model):
	name = models.CharField(max_length=50, default='foto')
	foto = models.ImageField(upload_to='photos/', blank=True, null=True)
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

	def __str__(self):
		return self.name