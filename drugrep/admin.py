from django.contrib import admin
from .models import DrugCompany, Drug, DrugNDC, Division, Manager, DrugRep


admin.site.register(DrugCompany)
admin.site.register(Drug)
admin.site.register(DrugNDC)
admin.site.register(Division)
admin.site.register(Manager)
admin.site.register(DrugRep)