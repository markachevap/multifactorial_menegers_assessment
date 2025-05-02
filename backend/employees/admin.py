from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Department, User
from django.apps import AppConfig

class EmployeesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employees'
    verbose_name = 'Сотрудники'

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                   'position', 'department', 'is_manager', 'is_hr')
    list_filter = ('is_manager', 'is_hr', 'is_admin', 'department')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'email')}),
        ('Рабочая информация', {'fields': ('position', 'department', 'hire_date')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'is_manager', 'is_hr', 'is_admin',
                                     'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(User, CustomUserAdmin)