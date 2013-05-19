from django.contrib import admin
from .models import Task, Category

admin.site.register(Category)

def mark_completed(modeladmin,request,queryset):
        queryset.update(is_completed=True)
mark_completed.short_description = "Mark Select Tasks Completed"

class TaskAdmin(admin.ModelAdmin):

    list_display = ['description','task_date','urgency','category','is_completed']
    list_filter = ['is_completed']
    actions = [mark_completed]

    def save_model(self, request, obj, form, change):
        """saves employee name who creates task, only if user is not an admin"""

        if not request.user.groups.filter(name='Rep Admin').count():
            obj.sales_rep = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        """Adds employee name field and shows employee in list display for Rep Admins"""

        if request.user.groups.filter(name='Rep Admin').count():
            self.fields = ['task_date','is_in_schedule','description','practice','category','is_completed','sales_rep']
            self.list_display.append('sales_rep')
        else:
            self.fields = ['task_date','is_in_schedule','description','practice','category','is_completed']
        return super(TaskAdmin, self).get_form(request, obj, **kwargs)


    def changelist_view(self, request, extra_context=None):
        """Only tasks for specific rep are shown, Rep Admin can see all tasks"""

        if not request.user.groups.filter(name='Rep Admin').count():
            q = request.GET.copy()
            q['sales_rep'] = request.user
            request.GET = q
            request.META['QUERY_STRING'] = request.GET.urlencode()
        return super(TaskAdmin,self).changelist_view(request, extra_context=extra_context)

admin.site.register(Task,TaskAdmin)
