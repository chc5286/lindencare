from django.contrib import admin
from .models import Task, Category

admin.site.register(Category)

def mark_completed(modeladmin,request,queryset):
        queryset.update(is_completed=True)
mark_completed.short_description = "Mark Select Tasks Completed"

class TaskAdmin(admin.ModelAdmin):

    list_display = ['description','urgency','category','is_completed']
    actions = [mark_completed]

    def save_model(self, request, obj, form, change):
        """saves employee name who creates task"""

        obj.sales_rep = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        """Adds employee name field for super users"""

        if request.user.is_superuser:
            self.fields = ['task_date','is_in_schedule','description','practice','category','is_completed','sales_rep']
        else:
            self.fields = ['task_date','is_in_schedule','description','practice','category','is_completed']
        return super(TaskAdmin, self).get_form(request, obj, **kwargs)



admin.site.register(Task,TaskAdmin)
