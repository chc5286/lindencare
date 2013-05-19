from django.contrib import admin
from .models import Task, Category

admin.site.register(Category)

class TaskAdmin(admin.ModelAdmin):
    fields = ['task_date','is_in_schedule','description','practice','category','is_completed']

    def save_model(self, request, obj, form, change):
        """saves employee name who creates task"""

        obj.sales_rep = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        """Adds employee name field for super users"""


        if request.user.is_superuser:
            self.fields.append('sales_rep')
        return super(TaskAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Task,TaskAdmin)
