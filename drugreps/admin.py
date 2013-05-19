from django.contrib import admin
from .models import DrugCompany, Drug, DrugNDC, Division, Manager, DrugRep


admin.site.register(DrugCompany)
admin.site.register(Drug)
admin.site.register(Division)


class DrugNdcAdmin(admin.ModelAdmin):
    fields = ['name','ndc','drug',('strength','strength_units')]

admin.site.register(DrugNDC,DrugNdcAdmin)


class DrugRepAdmin(admin.ModelAdmin):
    fields = [('first_name','last_name'),'manager','email','regions','comment','is_inactive']

admin.site.register(DrugRep,DrugRepAdmin)


class ManagerAdmin(admin.ModelAdmin):
    fields = [('first_name','last_name'),'division','email','territory','comment','is_inactive']

admin.site.register(Manager,ManagerAdmin)