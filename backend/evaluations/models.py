from django.db import models
from employees.models import User


class EvaluationWeights(models.Model):
    productivity_weight = models.FloatField("Вес производственных показателей", default=0.3)
    customer_satisfaction_weight = models.FloatField("Вес удовлетворенности клиентов", default=0.25)
    valid_from = models.DateField("Действует с")

    class Meta:
        verbose_name = "Вес критериев оценки"
        verbose_name_plural = "Веса критериев оценки"


class PerformanceEvaluation(models.Model):
    manager = models.ForeignKey(
        User,
        verbose_name="Менеджер",
        on_delete=models.CASCADE
    )
    period = models.CharField("Период", max_length=20)
    total_score = models.FloatField("Общий балл")
    comments = models.TextField("Комментарии", blank=True)

    class Meta:
        verbose_name = "Оценка эффективности"
        verbose_name_plural = "Оценки эффективности"
        unique_together = ['manager', 'period']