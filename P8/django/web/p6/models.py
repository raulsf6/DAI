from django.db import models
from django.utils import timezone

# Create your models here.

class Group(models.Model):
    id_group = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    style = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name

class Musician(models.Model):
    id_musician = models.AutoField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    birthday = models.DateTimeField(default = timezone.now)
    main_instrument = models.CharField(max_length=200)
    lat = models.CharField(max_length=200)
    lon = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Album(models.Model):
    id_album = models.AutoField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    distributor = models.CharField(max_length=200)
    release_Date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title