from django.contrib import admin

admin.site.site_header = "Система оценки менеджеров"
admin.site.site_title = "Администрирование"
admin.site.index_title = "Управление системой"

# Группировка в админке
admin.site.index_template = 'admin/custom_index.html'