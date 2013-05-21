from django.contrib import admin

from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):

    list_filter = ['is_complete']
    list_display =  ['practice','visit_date','comment','is_complete','sales_rep']
    list_editable = ['visit_date','is_complete']

    def save_model(self, request, obj, form, change):
        """saves employee name who creates task"""

        obj.sales_rep = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        """Adds employee name field for super users"""

        if request.user.groups.filter(name='Rep Admin').count():
            self.fields = ['practice','visit_date','comment','is_complete','sales_rep']
        else:
            self.fields = ['practice','visit_date','comment','is_complete']
        return super(AppointmentAdmin, self).get_form(request, obj, **kwargs)


    def changelist_view(self, request, extra_context=None):
        """Only appointments for specific rep are shown, superuser can see all tasks"""

        if not request.user.groups.filter(name='Rep Admin').count():
            q = request.GET.copy()
            q['sales_rep'] = request.user
            request.GET = q
            request.META['QUERY_STRING'] = request.GET.urlencode()
        return super(AppointmentAdmin,self).changelist_view(request, extra_context=extra_context)


admin.site.register(Appointment,AppointmentAdmin)



