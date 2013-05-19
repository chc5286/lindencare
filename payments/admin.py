from django.contrib import admin
from .models import Batch , Check, PaymentTransaction, PaymentType


admin.site.register(Batch)
admin.site.register(Check)
admin.site.register(PaymentTransaction)
admin.site.register(PaymentType)



