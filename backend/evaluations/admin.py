from django.contrib import admin
from .models import EvaluationWeights, PerformanceEvaluation, EvaluationFactor, FactorValue
from django.apps import AppConfig


class EvaluationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'evaluations'
    verbose_name = 'Оценки эффективности'

@admin.register(EvaluationWeights)
class EvaluationWeightsAdmin(admin.ModelAdmin):
    list_display = ('id', 'productivity_weight', 'customer_satisfaction_weight', 'valid_from')
    list_editable = ('productivity_weight', 'customer_satisfaction_weight')
    list_display_links = ('id',)
    ordering = ('-valid_from',)

@admin.register(PerformanceEvaluation)
class PerformanceEvaluationAdmin(admin.ModelAdmin):
    list_display = ('manager', 'period', 'total_score')
    list_filter = ('period', 'manager__department')
    search_fields = ('manager__first_name', 'manager__last_name')
    readonly_fields = ('total_score',)
    ordering = ('-period',)

@admin.register(EvaluationFactor)
class EvaluationFactorAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight')

@admin.register(FactorValue)
class FactorValueAdmin(admin.ModelAdmin):
    list_display = ('manager', 'factor', 'period', 'value')
    list_filter = ('period', 'factor', 'manager')