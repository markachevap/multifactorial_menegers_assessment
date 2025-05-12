from django.contrib import admin
from .models import Manager
from django.apps import AppConfig


class ManagersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'managers'
    verbose_name = 'Менеджеры'

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_department', 'level', 'specialization')
    list_filter = ('level', 'user__department')
    search_fields = ('user__first_name', 'user__last_name', 'specialization')
    raw_id_fields = ('user',)

    def get_department(self, obj):
        return obj.user.department

    get_department.short_description = 'Отдел'
    get_department.admin_order_field = 'user__department'