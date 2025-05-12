from django.contrib import admin
from django.urls import path, include
from evaluations.views import EvaluationListView, EvaluationCreateView, EvaluationDeleteView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EvaluationListView.as_view(), name='evaluation_list'),
    path('create/', EvaluationCreateView.as_view(), name='evaluation_create'),
    path('delete/<int:pk>/', EvaluationDeleteView.as_view(), name='evaluation_delete'),
    path('accounts/login/', LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]