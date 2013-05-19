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
        (None,              {'fields':['name','sub_region','category']}),
        ('Potential',       {'fields':[('ideal_visits','potential')]}),
        ('Yes/No',          {'fields':['is_inactive']}),
        ('Other',           {'fields':['drug_rep',('comment','next_visit')]}),
        ('Address',         {'fields':['address','address2',('city','state','zip_code')],'classes':['collapse']})
        ]

    inlines = [DoctorInLine,PracticeContactInLine,]


    list_display = ['name','sub_region','ideal_visits','potential','is_inactive']

admin.site.register(Practice, PracticeAdmin)
