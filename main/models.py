from django.db import models

# Create your models here.

class SpeedModel(models.Model):
	#pk = models.IntegerField(auto_increment=True)
	title = models.CharField(max_length=255)
	info = models.TextField()
	image = models.ImageField(upload_to='image')
