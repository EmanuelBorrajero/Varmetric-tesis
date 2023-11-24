from django.shortcuts import get_object_or_404
from .models import Scale, Variable, Dimension, Indicator, MeasurementCriterion
from .calculation import calculate_intervals

def calculateCriterionMax(indicator_id):
    indicator=get_object_or_404(Indicator, id=indicator_id)
    criterions = MeasurementCriterion.objects.filter(indicator=indicator)
    indicator_value=0
    criterions_value=0
    for criterion in criterions:
        criterions_value+=criterion.max_value
    indicator_value = indicator.weigh * criterions_value
    return indicator_value

def calculateCriterionMin(indicator_id):
    indicator=get_object_or_404(Indicator, id=indicator_id)
    criterions = MeasurementCriterion.objects.filter(indicator=indicator)
    indicator_value=0
    criterions_value=0
    for criterion in criterions:
        criterions_value+=criterion.min_value
    indicator_value = indicator.weigh * criterions_value
    return indicator_value
 
def calculateIndicatorMax(dimension_id):
    dimension=get_object_or_404(Dimension, id=dimension_id)
    indicators=Indicator.objects.filter(dimension=dimension)
    dimension_value=0
    indicators_value=0
    for indicator in indicators:
        indicators_value+=calculateCriterionMax(indicator.id)
    dimension_value = dimension.weigh * indicators_value
    return dimension_value

def calculateIndicatorMin(dimension_id):
    dimension=get_object_or_404(Dimension, id=dimension_id)
    indicators=Indicator.objects.filter(dimension=dimension)
    dimension_value=0
    indicators_value=0
    for indicator in indicators:
        indicators_value+=calculateCriterionMin(indicator.id)
    dimension_value = dimension.weigh * indicators_value
    return dimension_value

def calculateVariableMax(variable_id):
    variable=get_object_or_404(Variable, id=variable_id)
    dimensions=Dimension.objects.filter(variable=variable)
    variable_value=0
    for dimension in dimensions:
        variable_value+=calculateIndicatorMax(dimension.id)
    print(variable_value)
    return variable_value

def calculateVariableMin(variable_id):
    variable=get_object_or_404(Variable, id=variable_id)
    dimensions=Dimension.objects.filter(variable=variable)
    variable_value=0
    for dimension in dimensions:
        variable_value+=calculateIndicatorMin(dimension.id)
    print(variable_value)
    return variable_value


def createScale(count:int, var_id):
    min = calculateVariableMin(var_id)
    max = calculateVariableMax(var_id)
    intervalo = calculate_intervals(min,max,count)
    for n in range(int(count)):
        variable = get_object_or_404(Variable, id=var_id)
        Scale.objects.create(
            initial_value = intervalo[n][0],
            final_value = intervalo[n][1],
            scale = variable,
        )
