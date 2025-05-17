from .models import FactorValue, EvaluationFactor, PerformanceEvaluation
from employees.models import User

def calculate_evaluations(period: str):
    managers = User.objects.filter(is_manager=True)
    factors = EvaluationFactor.objects.all()

    weights = [f.weight for f in factors]
    weight_sum = sum(weights)
    normalized_weights = [w / weight_sum for w in weights]

    manager_values = []

    for manager in managers:
        row = []
        for factor in factors:
            try:
                val = FactorValue.objects.get(manager=manager, factor=factor, period=period).value
            except FactorValue.DoesNotExist:
                val = 0.0
            row.append(val)
        manager_values.append(row)

    # Внутрифакторная нормализация
    factor_scores = []
    for i in range(len(factors)):
        col = [row[i] for row in manager_values]
        total = sum(col) or 1.0
        factor_scores.append([v / total for v in col])

    # Итоговый расчет
    final_scores = []
    for i, manager in enumerate(managers):
        total = 0
        for j in range(len(factors)):
            total += factor_scores[j][i] * normalized_weights[j]
        final_scores.append((manager, total))

        # Сохраняем результат
        PerformanceEvaluation.objects.update_or_create(
            manager=manager,
            period=period,
            defaults={'total_score': total}
        )

    return final_scores
