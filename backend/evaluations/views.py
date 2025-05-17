from django.views.generic import ListView, CreateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import PerformanceEvaluation, FactorValue
from employees.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import calculate_evaluations
from .forms import FactorValueForm, EvaluationPeriodForm
from django.shortcuts import redirect

class EvaluationListView(LoginRequiredMixin, ListView):
    model = PerformanceEvaluation
    template_name = 'evaluations/evaluation_list.html'
    context_object_name = 'evaluations'

    def get_queryset(self):
        return PerformanceEvaluation.objects.all().select_related('manager')

class EvaluationCreateView(LoginRequiredMixin, CreateView):
    model = PerformanceEvaluation
    template_name = 'evaluations/evaluation_form.html'
    fields = ['manager', 'period', 'total_score', 'comments']
    success_url = reverse_lazy('evaluation_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['managers'] = User.objects.filter(is_manager=True)
        return context

    def post(self, request, *args, **kwargs):
        period = request.POST.get('period')
        calculate_evaluations(period)
        return HttpResponseRedirect(self.success_url)

class EvaluationDeleteView(LoginRequiredMixin, DeleteView):
    model = PerformanceEvaluation
    success_url = reverse_lazy('evaluation_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        if request.htmx:
            return HttpResponseRedirect(self.success_url)
        return super().delete(request, *args, **kwargs)

class FactorValueCreateView(LoginRequiredMixin, CreateView):
    model = FactorValue
    form_class = FactorValueForm
    template_name = 'evaluations/factor_value_form.html'
    success_url = reverse_lazy('add_factor_value')

class EvaluationRunView(LoginRequiredMixin, FormView):
    form_class = EvaluationPeriodForm
    template_name = 'evaluations/run_evaluation.html'
    success_url = reverse_lazy('evaluation_list')

    def form_valid(self, form):
        period = form.cleaned_data['period']
        calculate_evaluations(period)
        return super().form_valid(form)