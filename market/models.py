from django.db import models

# Create your models here.
class Items(models.Model):
	name = models.CharField(max_length=30)
	slot = models.CharField(max_length=30)
	gold = models.IntegerField()
	count = models.IntegerField()
	usable = models.CharField(max_length=30)
	bonus = models.CharField(max_length=30)
	prosperity = models.IntegerField()
	