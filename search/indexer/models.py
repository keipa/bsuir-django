from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField


class Forward(models.Model):
    link = models.TextField()
    text = models.TextField()
    title = models.TextField()
    number_of_words = models.IntegerField()

    def __str__(self):
        return self.link

class Inverted(models.Model):
    word = models.TextField(blank=True)
    link = models.TextField(blank=True)
    entries = models.IntegerField(default = 1) 
    
    def __str__(self):
        return self.word


# Create your models here.
