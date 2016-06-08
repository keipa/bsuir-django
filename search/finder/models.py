from __future__ import unicode_literals

from django.db import models


class SearchResult(models.Model):
    bigname = models.CharField(max_length=100)
    # link = models.permalink()
    description = models.CharField(max_length=300)
    count_of_coincidence = models.TextField()

    def __str__(self):
        return self.bigname






# Create your models here.
