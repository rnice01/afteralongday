from django.db import models

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=75)
    feedback = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    display = models.BooleanField(default=False)

    def __str__(self):
        return self.feedback