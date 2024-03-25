from django.db import models



class movie(models.Model):
    name = models.CharField(max_length=200)
    img=models.ImageField(upload_to='galary')
    des = models.TextField()
    year=models.DateField()
    actors=models.CharField(max_length=200)
    category=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class review(models.Model):
    movie = models.ForeignKey('movie', on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    comments = models.TextField()
    rating = models.IntegerField()