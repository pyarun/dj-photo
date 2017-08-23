# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Photo(models.Model):
    user = models.ForeignKey(User)
    # path=models.FilePathField(max_length=1024)
    file = models.FileField()
    name=models.CharField(max_length=50, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    archive= models.BooleanField(default=False)
    slug = models.SlugField()

    def __unicode__(self):
        return str(self.id)

    # def __str__(self):
    #     return self.__unicode__()
    #
    # def __repr__(self):
    #     return self.__unicode__()


class AlbumPhotos(models.Model):
    photo = models.ForeignKey(Photo)
    album = models.ForeignKey("Album")
    seq = models.IntegerField(null=True, blank=True)


class Album(models.Model):
    user = models.ForeignKey(User)
    name=models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    photos = models.ManyToManyField(Photo, blank=True, through=AlbumPhotos)

    def __unicode__(self):
        return str(self.name)



