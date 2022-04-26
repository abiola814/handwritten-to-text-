from django.db import models

# Create your models here.

class Register(models.Model):
	text = models.FileField(upload_to='specs')
	 
	 

class Dart(models.Model):
	text = models.CharField(max_length=100000)
	
