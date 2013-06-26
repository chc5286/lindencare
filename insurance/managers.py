from django.db import Models

from .models import BinNumber, Payor, Insuror


class InsuranceBinPayorManager(models.Manager):

    def insurance_bin_payor(self):
        return self.filter()

