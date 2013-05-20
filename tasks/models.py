import datetime
from django.db import models
from django.contrib.auth.models import User
from practices.models import Practice


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
    practice = models.ForeignKey(Practice,null=True,blank=True)
    category = models.ForeignKey(Category,null=True,blank=True)
    urgency = models.CharField(choices=URGENCY_CHOICES,default=LOW,max_length = 200)
    sales_rep = models.ForeignKey(User,null=True)
    

    def __unicode__(self):
        return self.description

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.is_in_schedule and not self.category:
            raise ValidationError('Must include category if task is in schedule')


