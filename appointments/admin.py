from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        """saves employee name who creates task"""

        obj.sales_rep = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        """Adds employee name field for super users"""

        if request.user.is_superuser:
            self.fields = ['practice','visit_date','comment','is_complete','sales_rep']
        else:
            self.fields = ['practice','visit_date','comment','is_complete']
        return super(AppointmentAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Appointment,AppointmentAdmin)



