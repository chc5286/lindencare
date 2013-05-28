from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    name = models.CharField(max_length=200,unique=True)

    def __unicode__(self):
        return self.name


class SubRegion(models.Model):
    name = models.CharField(max_length=200)
    region = models.ForeignKey(Region)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sub-Regions"