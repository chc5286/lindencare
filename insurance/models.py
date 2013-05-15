from django.db import models


class Payor(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __unicode__(self):
        return self.name

class BinNumber(models.Model):
    bin_number = models.IntegerField()
    payor = models.ForeignKey(Payor)

    def __unicode__(self):
        return self.bin_number

    class Meta:
        verbose_name_plural = 'Bin Numbers'

class Insuror(models.Model):
    carrier_code = models.CharField(max_length=2)
    plan_code = models.CharField(max_length=20,blank=True)
    bin_number = models.ForeignKey(BinNumber)

    def __unicode__(self):
        return self.carrier_code + ' ' + self.plan_code

