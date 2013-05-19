from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        """saves employee name who creates task"""

        obj.sales_rep = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        """Hides employee name from individual employees, available to see by all super users"""


        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('sales_rep')
        return super(AppointmentAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Appointment,AppointmentAdmin)



