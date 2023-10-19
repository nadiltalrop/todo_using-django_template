from django.contrib import admin

from.models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'priority','date')

admin.site.register(Task, TaskAdmin)