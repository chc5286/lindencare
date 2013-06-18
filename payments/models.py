from django.db import models

from insurance.models import Payor
from prescriptions.models import ScriptTransaction
from django.contrib.auth.models import User


class Batch(models.Model):
    code = models.CharField(max_length=8)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date_deposited = models.DateField()
    date_added = models.DateField() #use 3rd party module for this
    entered_by = models.ForeignKey(User)


    def __unicode__(self):
        return self.code

    class Meta:
        verbose_name_plural = 'Batches'


class Check(models.Model):
    check_number = models.CharField(max_length=40)
    payor = models.ForeignKey(Payor,null=True,blank=True)
    date = models.DateField()
    date_deposited = models.DateField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    fee = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    batch = models.ForeignKey(Batch,null=True,blank=True)
    entered_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.check_number


class PaymentType(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Payment Types'


class PaymentTransaction(models.Model):
    script_transaction = models.ForeignKey(ScriptTransaction)
    check = models.ForeignKey(Check)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    payment_type = models.ForeignKey(PaymentType)
    date_received = models.DateField()
    date_added = models.DateField() #use 3rd party module for this
    entered_by = models.ForeignKey(User,null=True,blank=True)

    def __unicode__(self):
        return self.script_transaction #script_number, refill_number, carrier_code + plan_code, amount

    class Meta:
        verbose_name_plural = 'Payment Transactions'







