from django.db import models
from django.urls import reverse

class Icecream(models.Model):
    flavor = models.CharField(max_length=255)

    def __str__(self):
        return self.flavor

    def get_absolute_url(self):
        return reverse('icecream:index')
# Create your models here.
