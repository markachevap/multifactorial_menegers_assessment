from django.contrib import admin
from .models import ProductivityMetrics, CustomerSatisfaction
from django.apps import AppConfig

class MetricsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'metrics'
    verbose_name = 'Метрики эффективности'

class ProductivityMetricsAdmin(admin.ModelAdmin):
    list_display = ('manager', 'date', 'deals_closed',
                   'revenue_generated', 'efficiency_score')
    list_filter = ('date', 'manager__department')
    date_hierarchy = 'date'
    search_fields = ('manager__first_name', 'manager__last_name')
    ordering = ('-date',)

class CustomerSatisfactionAdmin(admin.ModelAdmin):
    list_display = ('manager', 'date', 'survey_score', 'nps_score')
    list_filter = ('date', 'manager__department')
    date_hierarchy = 'date'
    search_fields = ('manager__first_name', 'manager__last_name')

admin.site.register(ProductivityMetrics, ProductivityMetricsAdmin)
admin.site.register(CustomerSatisfaction, CustomerSatisfactionAdmin)