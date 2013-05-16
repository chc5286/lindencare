from django.contrib import admin
from .models import Task, Category

class TaskAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.sales_rep = request.user
        obj.save()


admin.site.register(Task,TaskAdmin)
admin.site.register(Category)