from django.contrib import admin
from .models import *


# Register your models here.
class ProgramAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Program._meta.fields]


class TeamAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Team._meta.fields]


class CustomerProgramAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomerProgram._meta.fields]


class DeveloperAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Developer._meta.fields]


class CustomerProgramExecutionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomerProgramExecution._meta.fields]

admin.site.register(Program, ProgramAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(CustomerProgram, CustomerProgramAdmin)
admin.site.register(Developer, DeveloperAdmin)
admin.site.register(CustomerProgramExecution, CustomerProgramExecutionAdmin)

