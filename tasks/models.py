import datetime
from django.db import models
from django.conf import settings
from practices.models import Practice
from salesrep.models import SalesRep

class Category(models.Model):
    description = models.CharField(max_length = 200,unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.description

class Task(models.Model):
    """Tasks for each sales rep"""

    LOW = 'low'
    MEDIUM='medium'
    HIGH='high'
    URGENCY_CHOICES = (
         (LOW,"Low"),
         (MEDIUM,"Medium"),
         (HIGH,"High")
    )

    task_date = models.DateTimeField(default=datetime.datetime.now())
    description = models.TextField()
    is_completed = models.BooleanField("Completed?")
    is_in_schedule = models.BooleanField("In Schedule?")
    practice = models.ForeignKey(Practice,null=True)
    category = models.ForeignKey(Category,null=True)
    urgency = models.CharField(choices=URGENCY_CHOICES,default=LOW,max_length = 200)
    sales_rep = models.ForeignKey(SalesRep,null=True) #use settings.AUTH_USER_MODEL once user model is set up
    

    def __unicode__(self):
        return self.description

