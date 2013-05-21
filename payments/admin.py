from django.contrib import admin

from .models import Batch , Check, PaymentTransaction, PaymentType


admin.site.register(Batch)
admin.site.register(PaymentType)


class CheckAdmin(admin.ModelAdmin):
    fields = ['check_number','payor','batch','amount','fee','date','date_deposited']

admin.site.register(Check,CheckAdmin)


class PaymentTransactionAdmin(admin.ModelAdmin):
    fields = ['script_transaction','payment_type','amount','check','date_received']

admin.site.register(PaymentTransaction,PaymentTransactionAdmin)