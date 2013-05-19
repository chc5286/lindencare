from django.contrib import admin
from .models import Patient


class PatientAdmin(admin.ModelAdmin):
    fields = [('first_name','last_name'),'commission_tag','email','comment','address','address2',('city','state','zip_code'),'is_inactive']

admin.site.register(Patient,PatientAdmin)


