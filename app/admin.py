from django.contrib import admin

# Register your models here.

from app.models import *

class Custom1(admin.ModelAdmin):
    list_display = ['sname','sprincipal','slocation']

class Custom2(admin.ModelAdmin):
    list_display = ['stdname','stdage']

admin.site.register(School,Custom1)
admin.site.register(Student,Custom2)