from django.db import models
from core.models import Person, Contact, Address
from salesrep.models import CommissionTag
from drugrep.models import DrugRep
from region.models import SubRegion

class MultiPractice(models.Model):
    name = models.CharField(max_length = 200,unique=True)

    def __unicode__(self):
        return self.name
	
class Category(models.Model):
    description = models.CharField(max_length = 200,unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.description


class Practice(Address):
    name = models.CharField(max_length = 200,unique=True)
    multi_practice = models.ForeignKey(MultiPractice,null=True)
    ideal_visits = models.IntegerField(default=0)
    potential = models.FloatField(null=True)
    is_inactive = models.BooleanField(default=False)
    comment = models.TextField(blank=True)
    next_visit = models.TextField(blank=True)
    category = models.ManyToManyField(Category,null=True)
    drug_rep = models.ManyToManyField(DrugRep,verbose_name="Drug Rep",null=True)
    sub_region = models.ForeignKey(SubRegion,verbose_name="Sub-Region",null=True)
    #phone
    #fax

    def __unicode__(self):
        return self.name
	
class ContactType(models.Model):
    description = models.CharField(max_length = 200,unique=True)

    class Meta:
        verbose_name_plural = "Contact Types"

    def __unicode__(self):
        return self.description


class Doctor(Contact):
    practice = models.ForeignKey(Practice)  
    opus_key = models.IntegerField(unique=True)
    commission_tag = models.ForeignKey(CommissionTag,null=True)

    def doctorName(self):
        return 'Dr. ' + self.first_name.title() + ' ' + self.last_name.title()
    doctorName.short_description = 'Doctor'

    def __unicode__(self):
        return self.fullName


class PracticeContact(Contact):
    practice = models.ForeignKey(Practice)
    contact_type = models.ForeignKey(ContactType)
    
    def __unicode__(self):
        return self.fullName
    
    


