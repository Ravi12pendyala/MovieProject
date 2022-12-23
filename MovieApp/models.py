from django.db import models
#Create your models here.
class Movies(models.Model):
    releasedate=models.DateField()
    moviename=models.CharField(max_length=30)
    hero=models.CharField(max_length=30)
    heroin=models.CharField(max_length=30)
    rating=models.IntegerField()
