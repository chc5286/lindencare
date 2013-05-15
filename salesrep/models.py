#from django.conf import settings
#from django.contrib.auth.models import AbstractBaseUser
from django.db import models
#from django.utils.translation import ugettext_lazy as _
from core.models import Contact

"""
class SalesRep(AbstractBaseUser,Contact):
     Need this model to be for the Linden Care staff. Should have login/password

"""

class SalesRep(Contact):


    def __unicode__(self):
        return self.username

	
class CommissionTag(models.Model):
    tag = models.CharField(max_length=3,unique=True)

    def __unicode__(self):
        return self.tag
	
class CommissionTagSplit(models.Model):
    sales_rep = models.ForeignKey(SalesRep) #use settings.AUTH_USER_MODEL once user model is set up
    commission_tag = models.ForeignKey(CommissionTag)
    commission_percent = models.FloatField()
    is_inactive = models.BooleanField()
	

