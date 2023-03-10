from django.db import models
from django.contrib.auth.models import User as UserAuth

class User(models.Model):
    user = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    rol= models.CharField(max_length=40)
    email = models.EmailField()
    avatar = models.CharField(max_length= 250)


class Movie(models.Model):
    title =  models.CharField(max_length=40)
    img =  models.ImageField()
    description = models.CharField(max_length=500)
    tag = models.CharField(max_length=40)


class Review(models.Model):
    title =  models.CharField(max_length=40)
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField()
def __str__(self):
        return f'Review de MovieUser: {self.user}'

class Avatar(models.Model):
    user = models.OneToOneField(UserAuth, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __srt__(self):
        return self.user.user