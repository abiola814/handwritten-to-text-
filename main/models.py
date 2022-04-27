from django.db import models

# Create your models here.

class Register(models.Model):
	text = models.FileField(upload_to='specs')
	 
	 

class Dart(models.Model):
	text = models.TextField(max_length=1000000)


class GetImage(models.Model):   
    img = models.ImageField(upload_to="media")
    class Meta:
        db_table = "gallery"	
