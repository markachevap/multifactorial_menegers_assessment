from django.contrib import admin
from .models import ClientFeedback, PeerReview
from django.apps import AppConfig


class FeedbackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'feedback'
    verbose_name = 'Обратная связь'

@admin.register(ClientFeedback)
class ClientFeedbackAdmin(admin.ModelAdmin):
    list_display = ('manager', 'date', 'rating', 'short_comment')
    list_filter = ('date', 'rating', 'manager__department')
    date_hierarchy = 'date'
    search_fields = ('manager__first_name', 'manager__last_name', 'comment')

    def short_comment(self, obj):
        return obj.comment[:50] + '...' if len(obj.comment) > 50 else obj.comment

    short_comment.short_description = 'Комментарий'


@admin.register(PeerReview)
class PeerReviewAdmin(admin.ModelAdmin):
    list_display = ('manager', 'reviewer', 'score')
    list_filter = ('manager__department',)
    search_fields = ('manager__first_name', 'manager__last_name',
                     'reviewer__first_name', 'reviewer__last_name')
    raw_id_fields = ('manager', 'reviewer')