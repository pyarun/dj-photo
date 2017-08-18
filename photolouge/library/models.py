# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Photo(models.Model):
    # path=models.FilePathField(max_length=1024)
    file = models.FileField()
    name=models.CharField(max_length=50, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    archive= models.BooleanField(default=False)
    slug = models.SlugField()

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()