from django.db import models

from core.models import Contact, Address
from salesreps.models import CommissionTag
from drugcompanies.models import DrugRep
from regions.models import SubRegion

class MultiPractice(models.Model):
    name = models.CharField(max_length = 200,unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Multi-Practices"


class Category(models.Model):
    description = models.CharField(max_length = 200,unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.description


class Practice(Address):
    name = models.CharField(max_length = 200,unique=True)
    multi_practice = models.ForeignKey(MultiPractice,null=True,blank=True)
    ideal_visits = models.IntegerField(default=0)
    potential = models.FloatField(null=True,blank=True)
    is_inactive = models.BooleanField("Inactive?")
    comment = models.TextField(blank=True)
    next_visit = models.TextField(blank=True)
    category = models.ManyToManyField(Category,null=True,blank=True)
    drug_rep = models.ManyToManyField(DrugRep,verbose_name="Drug Rep",null=True,blank=True)
    sub_region = models.ForeignKey(SubRegion,verbose_name="Sub-Region",null=True,blank=True)

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
    opus_key = models.IntegerField(null=True,blank=True,default=1001)
    commission_tag = models.ForeignKey(CommissionTag,null=True)

    def doctor_name(self):
        return 'Dr. ' + self.first_name.title() + ' ' + self.last_name.title()

    def __unicode__(self):
        return self.doctor_name()


class PracticeContact(Contact):
    practice = models.ForeignKey(Practice)
    contact_type = models.ForeignKey(ContactType)
    
    #def __unicode__(self):
        #return self.full_name

    class Meta:
        verbose_name_plural = "Practice Contacts"
    


