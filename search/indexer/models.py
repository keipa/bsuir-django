from __future__ import unicode_literals

from django.db import models

class Link(models.Model):
    link = models.CharField(max_length=100)
    text = models.TextField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.link



# Create your models here.
