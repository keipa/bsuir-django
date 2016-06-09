from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField


class Forward(models.Model):
    link = models.CharField(max_length=100)
    text = models.TextField()
    title = models.CharField(max_length=100)
    number_of_words = models.IntegerField()

    def __str__(self):
        return self.link

class Inverted(models.Model):
    word = models.CharField(max_length=50)
    link = models.TextField(blank=True)
    entries = models.IntegerField(default = 1) 
    
    def __str__(self):
        return self.word


# Create your models here.
