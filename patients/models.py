from django.db import models

from core.models import Contact, Address
from salesreps.models import CommissionTag

class Patient(Contact,Address):
    opus_key = models.IntegerField()
    commission_tag = models.ForeignKey(CommissionTag,null=True,blank=True)

