from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'submitted_by', 'created_at')
    search_fields = ('title', 'description', 'submitted_by')
