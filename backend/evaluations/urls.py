from django.urls import path
from .views import (
    EvaluationCreateView,
    FactorValueCreateView,
    EvaluationRunView,
)

urlpatterns = [
    path('add/', EvaluationCreateView.as_view(), name='evaluation_add'),
    path('factors/add/', FactorValueCreateView.as_view(), name='add_factor_value'),
    path('run/', EvaluationRunView.as_view(), name='run_evaluation'),
]
