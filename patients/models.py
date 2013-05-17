from django.db import models
from core.models import Person, Address
from salesreps.models import CommissionTag

class Patient(Person,Address):
    opus_key = models.IntegerField()
    commission_tag = models.ForeignKey(CommissionTag,null=True,blank=True)

    #def __unicode__(self):
        #return self.full_name