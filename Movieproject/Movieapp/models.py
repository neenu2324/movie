from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
#

    def __str__(self):
        return self.name

class movie(models.Model):
    name = models.CharField(max_length=200)
    img=models.ImageField(upload_to='galary')
    des = models.TextField()
    year=models.DateField(null=True,blank=True)
    actors=models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
#
#
class review(models.Model):
    movie = models.ForeignKey('movie', on_delete=models.CASCADE)
    comments = models.TextField()
    rating = models.IntegerField()
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
