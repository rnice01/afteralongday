import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    user = models.OneToOneField(User, null=True)
    text = models.TextField(default='Add your comment here.')
    date_posted = models.DateField(auto_now_add=True)

class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField(null=True)
    published = models.DateField(auto_now_add=True)
    favorited = models.ManyToManyField(User)
    comments = models.ManyToManyField(Comment)
    image_url = models.TextField(default=settings.STATIC_URL + 'image/bathbombs/makeitmine.jpg')

    def __str__(self):
        return self.title

    def times_favorited(self):
        if self.favorited is not None:
            return self.favorited.count()
        return ""

class Reply(models.Model):
    user = models.ManyToManyField(User)
    reply = models.TextField(default='Add your reply here.')
    date_posted = models.DateField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)