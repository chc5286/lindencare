from django.db import models

from core.models import Contact, Address
from salesreps.models import CommissionTag

class Patient(Contact,Address):
    opus_key = models.IntegerField(null=True,blank=True,default=0)
    commission_tag = models.ForeignKey(CommissionTag,null=True,blank=True)

