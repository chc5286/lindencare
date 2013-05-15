from django.db import models
from core.models import Person, Address
from salesrep.models import CommissionTag

class Patient(Person,Address):
    opus_key = models.IntegerField()
    commission_tag = models.ForeignKey(CommissionTag)

    def __unicode__(self):
        return self.fullName
