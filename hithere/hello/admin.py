from django.contrib import admin

# Register your models here.
from hello.models import Task,CompletedTask
admin.site.register(Task)
admin.site.register(CompletedTask)