from django.db.models import Sum, Count
from .models import Variable, Dimension, Indicator, MeasurementCriterion
from Apps.Instruments.models import AnswerPoll, AnswerInterview, ObservationResult

def calculate_intervals(min_value, max_value, cant_intervals:int):
    iterator = 0
    intervals_list = []
    if min_value < max_value and int(cant_intervals) > 2:
        initial_interval_value = float(min_value)
        terminal_interval_value = initial_interval_value + \
            float((max_value / int(cant_intervals)))
        interval = [initial_interval_value, terminal_interval_value]
        intervals_list.append(interval)
        while(iterator != int(cant_intervals) - 2):
            initial_interval_value = terminal_interval_value + 0.0001
            terminal_interval_value = float(initial_interval_value) + \
                float((max_value / int(cant_intervals)))
            interval = [initial_interval_value, terminal_interval_value]
            intervals_list.append(interval)
            iterator += 1
        intervals_list.append([(terminal_interval_value + 0.0001), max_value])
        return intervals_list
    else:
        intervals_list.append("Valores Errónios")
    return intervals_list


def calcular_estado_variable(variable_id, user_id):
    variable = Variable.objects.get(id=variable_id)
    dimensions = Dimension.objects.filter(variable=variable)
    total_weighted_criterion_sum = 0
    total_weighted_indicator_sum = 0
    for dimension in dimensions:
        mi = Indicator.objects.filter(dimension=dimension).count()
        for indicator in Indicator.objects.filter(dimension=dimension):
            nij = MeasurementCriterion.objects.filter(indicator=indicator).count()
            if AnswerPoll.objects.filter(questionPoll__measurementCriterions__indicator=indicator, user_id=user_id).exists():
                total_weighted_criterion_sum += (indicator.weight / mi) * (AnswerPoll.objects.filter(questionPoll__measurementCriterions__indicator=indicator, user_id=user_id).aggregate(Sum('value'))['value__sum'] / nij)
            elif AnswerInterview.objects.filter(questionInterview__measurementCriterions__indicator=indicator, user_id=user_id).exists():
                total_weighted_criterion_sum += (indicator.weight / mi) * (AnswerInterview.objects.filter(questionInterview__measurementCriterions__indicator=indicator, user_id=user_id).aggregate(Sum('value'))['value__sum'] / nij)
            elif ObservationResult.objects.filter(observationCriterions__indicator=indicator, user_id=user_id).exists():
                total_weighted_criterion_sum += (indicator.weight / mi) * (ObservationResult.objects.filter(observationCriterions__indicator=indicator, user_id=user_id).aggregate(Sum('value'))['value__sum'] / nij)
            total_weighted_indicator_sum += indicator.weight / mi
    return total_weighted_criterion_sum / total_weighted_indicator_sum


