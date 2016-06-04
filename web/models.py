from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UrlRequest(models.Model):
    """
    The main course run every year. Resources are attached to it.
    """
    url = models.CharField(max_length=500)

    def __unicode__(self):
        return self.url

