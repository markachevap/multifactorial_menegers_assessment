from django import forms
from .models import FactorValue, EvaluationFactor
from employees.models import User

class FactorValueForm(forms.ModelForm):
    class Meta:
        model = FactorValue
        fields = ['manager', 'factor', 'period', 'value']

class EvaluationPeriodForm(forms.Form):
    period = forms.CharField(label="Период", max_length=20)
