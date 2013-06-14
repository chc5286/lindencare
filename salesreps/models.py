from django.db import models
from django.contrib.auth.models import User


class CommissionTag(models.Model):
    tag = models.CharField(max_length=3,unique=True)

    def __unicode__(self):
        return self.tag


class CommissionTagSplit(models.Model):
    sales_rep = models.ForeignKey(User)
    commission_tag = models.ForeignKey(CommissionTag)
    commission_percent = models.FloatField()
    is_inactive = models.BooleanField("Inactive?")

    def __unicode__(self):
        return str(self.commission_tag) + ' ' + str(self.commission_percent)

	

