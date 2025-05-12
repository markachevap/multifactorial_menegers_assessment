from django.db import models
from employees.models import Department


class KPI(models.Model):
    name = models.CharField("Название KPI", max_length=100)
    target_value = models.FloatField("Целевое значение")

    class Meta:
        verbose_name = "KPI"
        verbose_name_plural = "KPI"


class DepartmentReport(models.Model):
    department = models.ForeignKey(
        Department,
        verbose_name="Отдел",
        on_delete=models.CASCADE
    )
    period = models.DateField("Период", max_length=20)
    average_score = models.FloatField("Средний балл")

    class Meta:
        verbose_name = "Отчет по отделу"
        verbose_name_plural = "Отчеты по отделам"