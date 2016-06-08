from __future__ import unicode_literals

from django.db import models

class Forward(models.Model):
    link = models.CharField(max_length=100)
    text = models.TextField()
    title = models.CharField(max_length=100)
    number_of_words = models.IntegerField()

    def __str__(self):
        return self.link

class Inverted(models.Model):
	word = models.CharField(max_length=50)
	links = models.TextField()



# Create your models here.
