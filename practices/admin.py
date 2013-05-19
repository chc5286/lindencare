from django.contrib import admin
from .models import Practice, MultiPractice, Category, ContactType, Doctor, PracticeContact


admin.site.register(MultiPractice)
admin.site.register(Category)
admin.site.register(ContactType)
admin.site.register(PracticeContact)


class PracticeContactInLine(admin.TabularInline):
    model = PracticeContact
    extra = 1
    fields = ['first_name','last_name','email','contact_type','comment','is_inactive']

class DoctorAdmin(admin.ModelAdmin):
        fieldsets = [
        ('Name',              {'fields':['first_name','last_name']}),
        ('Practice',          {'fields':['practice']}),
        ('Contact Info',      {'fields':['email','is_inactive']}),
        ('Comment',           {'fields':['comment']}),
        ]

        list_display = ['doctorName','practice','is_inactive']

        search_fields = ['first_name','last_name']

admin.site.register(Doctor, DoctorAdmin)


class DoctorInLine(admin.TabularInline):
        model = Doctor
        extra = 1
        fields = ['first_name','last_name','email','commission_tag','comment','is_inactive']


class PracticeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['name','multi_practice']}),
        ('Potential',       {'fields':[('ideal_visits','potential')]}),
        ('Address',         {'fields':['sub_region','address','address2',('city','state','zip_code')],'classes':['collapse']}),
        ('Other',           {'fields':['drug_rep','category',('comment','next_visit')]}),
        ('Yes/No',          {'fields':['is_inactive']}),
        ]

    inlines = [DoctorInLine,PracticeContactInLine,]

    list_display = ['name','sub_region','ideal_visits','potential','is_inactive']
    search_fields = ['name']

admin.site.register(Practice, PracticeAdmin)
