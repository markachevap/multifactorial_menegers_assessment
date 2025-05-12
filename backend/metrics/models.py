from django.db import models
from employees.models import User


class ProductivityMetrics(models.Model):
    manager = models.ForeignKey(
        User,
        verbose_name="Менеджер",
        on_delete=models.CASCADE
    )
    date = models.DateField("Дата")
    deals_closed = models.IntegerField("Закрытые сделки", default=0)
    revenue_generated = models.DecimalField(
        "Выручка",
        max_digits=12,
        decimal_places=2,
        default=0
    )
    efficiency_score = models.FloatField("Оценка эффективности", default=0)

    class Meta:
        verbose_name = "Производственный показатель"
        verbose_name_plural = "Производственные показатели"
        indexes = [
            models.Index(fields=['manager', 'date']),
        ]


class CustomerSatisfaction(models.Model):
    manager = models.ForeignKey(
        User,
        verbose_name="Менеджер",
        on_delete=models.CASCADE
    )
    date = models.DateField("Дата")
    survey_score = models.FloatField("Оценка опроса", default=0)
    nps_score = models.FloatField("NPS", default=0)

    class Meta:
        verbose_name = "Удовлетворенность клиентов"
        verbose_name_plural = "Удовлетворенность клиентов"