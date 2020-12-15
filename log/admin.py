from django.contrib import admin
from .models import logPeople
# Register your models here.

class LogAdmin(admin.ModelAdmin):
	list_display = ['name', 'position', 'date']
	list_filter = ['date','name']
	search_fields = ['name']

admin.site.register(logPeople, LogAdmin)