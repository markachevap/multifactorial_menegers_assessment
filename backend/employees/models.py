from django.contrib.auth.models import AbstractUser
from django.db import models


class Department(models.Model):
    name = models.CharField("Название отдела", max_length=100)
    description = models.TextField("Описание", blank=True)

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"


class User(AbstractUser):
    is_manager = models.BooleanField("Менеджер", default=False)
    is_hr = models.BooleanField("HR", default=False)
    is_admin = models.BooleanField("Администратор", default=False)
    department = models.ForeignKey(
        Department,
        verbose_name="Отдел",
        on_delete=models.SET_NULL,
        null=True
    )
    position = models.CharField("Должность", max_length=100)
    hire_date = models.DateField("Дата приема", null=True, blank=True)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"