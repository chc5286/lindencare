from django.db import models
from insurance.models import Payor
from prescriptions.models import ScriptTransaction


class Batch(models.Model):
    code = models.CharField(max_length=8)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date_deposited = models.DateField()
    date_added = models.DateField() #use 3rd party module for this

    def __unicode__(self):
        return self.code


class Check(models.Model):
    check_number = models.CharField(max_length=40)
    payor = models.ForeignKey(Payor,null=True,blank=True)
    date = models.DateField()
    date_deposited = models.DateField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    fee = models.DecimalField(max_digits=10,decimal_places=2)
    batch = models.ForeignKey(Batch,null=True,blank=True)

    def __unicode__(self):
        return self.check_number


class PaymentType(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class PaymentTransaction(models.Model):
    script_transaction = models.ForeignKey(ScriptTransaction)
    check = models.ForeignKey(Check)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    payment_type = models.ForeignKey(PaymentType)
    received_date = models.DateField()
    date_added = models.DateField() #use 3rd party module for this

    def __unicode__(self):
        return self.script_transaction #script_number, refill_number, carrier_code + plan_code, amount







