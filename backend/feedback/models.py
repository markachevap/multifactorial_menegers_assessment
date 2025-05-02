from django.db import models
from employees.models import User


class ClientFeedback(models.Model):
    manager = models.ForeignKey(
        User,
        verbose_name="Менеджер",
        on_delete=models.CASCADE
    )
    date = models.DateField("Дата")
    comment = models.TextField("Отзыв")
    rating = models.PositiveSmallIntegerField("Оценка")

    class Meta:
        verbose_name = "Отзыв клиента"
        verbose_name_plural = "Отзывы клиентов"


class PeerReview(models.Model):
    reviewer = models.ForeignKey(
        User,
        verbose_name="Оценивающий",
        on_delete=models.CASCADE,
        related_name='given_reviews'
    )
    manager = models.ForeignKey(
        User,
        verbose_name="Менеджер",
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.FloatField("Оценка")

    class Meta:
        verbose_name = "Оценка коллег"
        verbose_name_plural = "Оценки коллег"