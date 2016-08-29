from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Words(models.Model):
    alpha = models.CharField(max_length=500)

    def __str__(self):
        return self.alpha
