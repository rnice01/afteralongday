import os
from django.conf import settings
from django.db import models
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField(null=True)
    published = models.DateField(auto_now_add=True)
    favorited = models.IntegerField(default=0)
    image = models.ImageField(upload_to='img/blog', null=True)

    def __str__(self):
        return self.title

    def image_file(self):
        if self.image is not None:
            return os.path.basename(self.image.name)
        return None

    def times_favorited(self):
        if self.favorited > 0:
            return self.favorited
        return ""

class Comment(models.Model):
    name = models.CharField(max_length=120)
    comment = models.TextField(default='Add your comment here.')
    date_posted = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Reply(models.Model):
    name = models.CharField(max_length=120)
    reply = models.TextField(default='Add your reply here.')
    date_posted = models.DateField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)