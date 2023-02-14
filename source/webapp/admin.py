from django.contrib import admin

from webapp.models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status', 'completion_date')
    list_filter = ('id', 'title', 'description', 'status', 'completion_date')
    search_fields = ('title', 'status')
    fields = ('title', 'description', 'status', 'completion_date')
    readonly_fields = ('id',)


admin.site.register(Task, TaskAdmin)
