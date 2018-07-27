from django.db import models

# Create your models here.

class MyItems(models.Model):
	head = models.CharField(max_length=50)
	body = models.CharField(max_length=50)
	legs = models.CharField(max_length=50)
	onehand = models.CharField(max_length=50)
	twohand = models.CharField(max_length=50)
	small = models.CharField(max_length=50)

class Items(models.Model):
	prosp = models.CharField(max_length=50)
	slot = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	modifier = models.CharField(max_length=50)
	cclass = models.CharField(max_length=50)
	