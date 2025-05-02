from django.contrib import admin
from .models import KPI, DepartmentReport
from django.apps import AppConfig


class AnalyticsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'analytics'
    verbose_name = 'Отчеты'

@admin.register(KPI)
class KPIAdmin(admin.ModelAdmin):
    list_display = ('name', 'target_value')
    list_editable = ('target_value',)
    search_fields = ('name',)



@admin.register(DepartmentReport)
class DepartmentReportAdmin(admin.ModelAdmin):
    list_display = ('department', 'period', 'average_score')
    list_filter = ('period', 'department')
    search_fields = ('department__name',)
    date_hierarchy = 'period'
    ordering = ('-period',)