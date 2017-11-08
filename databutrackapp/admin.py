from django.contrib import admin

# Register your models here.

from databutrackapp.models import Bugtrack

@admin.register(Bugtrack)
class BugtrackAdmin(admin.ModelAdmin):
    list_display = ('description','assign_to','created_by','priority','created_on',)

