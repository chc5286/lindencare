from django.db import models

class InteractionType(models.Model):
    name = models.TextField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Interaction Types'


class Interaction(models.Model):

    DOCTOR = 'doctor'
    MANAGER ='manager'
    DRUG_REP ='drug rep'
    PRACTICE = 'practice'
    TABLE_CHOICES = (
         (DOCTOR,"Doctor"),
         (MANAGER,"Manager"),
         (DRUG_REP,"Drug Rep"),
         (PRACTICE,"Practice")
    )


    date = models.DateField()
    type = models.ForeignKey(InteractionType,null=True,blank=True)
    table = models.CharField(choices=TABLE_CHOICES,max_length=20)
    person_id = models.IntegerField("Person")
    description = models.TextField(max_length=300)

    def __unicode__(self):
        return self.description