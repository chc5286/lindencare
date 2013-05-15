from django.db import models
from drugrep.models import DrugNDC
from salesrep.models import CommissionTag
from practices.models import Doctor
from patient.models import Patient
from insurance.models import Insuror


class Script(models.Model):
    """Model for prescriptions
    """

    opus_key = models.IntegerField()
    script_number = models.IntegerField()
    refill_number = models.IntegerField()
    date_of_service = models.DateField()
    deleted_date = models.DateField()
    drug_ndc = models.ForeignKey(DrugNDC)
    patient = models.ForeignKey(Patient)
    commission_tag = models.ForeignKey(CommissionTag)
    acquisition_price = models.DecimalField(max_digits=10,decimal_places=2)
    doctor = models.ForeignKey(Doctor)
    third_party_script = models.IntegerField()
    is_filled_by_robot = models.BooleanField()
    last_cash_posting_date = models.DateField()
    is_non_processed = models.BooleanField()

    def __unicode__(self):
        return str(self.script_number) + ' ' + str(self.refill_number)

class ScriptPayment(models.Model):
    """ Model for transactions made on scripts. Every adjustment, rebilling and
    deletion is handled here. All revenue is calculated from the amount field
    in this model.
    """

    opus_key = models.IntegerField()
    opus_table = models.CharField(max_length=10)
    transaction_date = models.DateField()
    insuror = models.ForeignKey(Insuror)
    payor_order = models.IntegerField()
    is_non_processed = models.BooleanField()
    deleted_date = models.DateField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)

    def __unicode__(self):
        return self.insurance #should change to related script/refill/insurance

    class Meta:
        verbose_name_plural = "Script Payments"






