from django.db import models
from employees.models import User


class Manager(models.Model):
    LEVEL_CHOICES = [
        ('junior', 'Младший'),
        ('middle', 'Средний'),
        ('senior', 'Старший'),
    ]

    user = models.OneToOneField(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        primary_key=True
    )
    level = models.CharField(
        "Уровень",
        max_length=10,
        choices=LEVEL_CHOICES,
        default='middle'
    )
    specialization = models.CharField("Специализация", max_length=100)

    class Meta:
        verbose_name = "Менеджер"
        verbose_name_plural = "Менеджеры"