from django.shortcuts import get_object_or_404
from .models import *
from Apps.Instruments.models import *

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
        return False
#Poll
def get_question_id_poll(answer_id):
    answer = get_object_or_404(AnswerPoll, id=answer_id)
    if answer:
        question_id = answer.questionPoll
        return question_id

def get_criterion_id_poll(question_id):
    question = get_object_or_404(QuestionPoll, id=question_id)
    if question:
        criterion_id = question.measurementCriterions
        return criterion_id

def get_indicator_poll(criterion_id):
    citerion = get_object_or_404(MeasurementCriterion, id=criterion_id)
    if citerion:
        indicator_id = citerion.indicator
        return indicator_id 

def get_dimension_poll(indicator_id):
    indicator = get_object_or_404(Indicator, id=indicator_id)
    if indicator:
        dimension_id = indicator.dimension
        return dimension_id

def get_variable_poll(answer_id):
    question_id = get_question_id_poll(answer_id=answer_id)
    criterion_id = get_criterion_id_poll(question_id=question_id)
    indicator_id = get_indicator_poll(criterion_id=criterion_id)
    dimension_id = get_dimension_poll(indicator_id=indicator_id)
    dimension = get_object_or_404(Dimension, id=dimension_id)
    variable_id = dimension.variable
    return variable_id 
    
def criterion_answerpoll_value(criterion_id, user_id):
    criterion = get_object_or_404(MeasurementCriterion, id=criterion_id)
    if criterion:
        question = get_object_or_404(QuestionPoll, measurementCriterions=criterion)
        poll_id = question.poll
        if question:
            answer = AnswerPoll.objects.filter(questionPoll__poll_id=poll_id, user=user_id)
            if answer:
                criterion_value = answer.value
            return criterion_value

def calculate_criterion_poll(indicator_id, user_id):
    indicator=get_object_or_404(Indicator, id=indicator_id)
    criterions = MeasurementCriterion.objects.filter(indicator=indicator)
    indicator_value=0
    if criterions:
        criterions_value=0
        for criterion in criterions:
            criterions_value+=criterion_answerpoll_value(criterion.id, user_id)
        indicator_value = indicator.weigh * criterions_value
        return indicator_value
    return indicator_value

def calculate_indicator_poll(dimension_id, user_id):
    dimension=get_object_or_404(Dimension, id=dimension_id)
    indicators=Indicator.objects.filter(dimension=dimension)
    dimension_value=0
    if indicators:
        indicators_value=0
        for indicator in indicators:
            indicators_value+=calculate_criterion_poll(indicator.id, user_id)
        dimension_value = dimension.weigh * indicators_value
        return dimension_value
    return dimension_value

def calculate_variable_poll(variable_id, user_id):
    variable=get_object_or_404(Variable, id=variable_id)
    dimensions=Dimension.objects.filter(variable=variable)
    variable_value=0
    if dimensions:
        for dimension in dimensions:
            variable_value+=calculate_indicator_poll(dimension.id, user_id)
        return variable_value
    return variable_value

#Interview
def get_question_id_interview(answer_id):
    answer = get_object_or_404(AnswerInterview, id=answer_id)
    if answer:
        question_id = answer.questionInterview
        return question_id

def get_criterion_id_interview(question_id):
    question = get_object_or_404(QuestionInterview, id=question_id)
    if question:
        criterion_id = question.measurementCriterions
        return criterion_id

def get_indicator_interview(criterion_id):
    citerion = get_object_or_404(MeasurementCriterion, id=criterion_id)
    if citerion:
        indicator_id = citerion.indicator
        return indicator_id 

def get_dimension_interview(indicator_id):
    indicator = get_object_or_404(Indicator, id=indicator_id)
    if indicator:
        dimension_id = indicator.dimension
        return dimension_id

def get_variable_interview(answer_id):
    question_id = get_question_id_interview(answer_id=answer_id)
    criterion_id = get_criterion_id_interview(question_id=question_id)
    indicator_id = get_indicator_interview(criterion_id=criterion_id)
    dimension_id = get_dimension_interview(indicator_id=indicator_id)
    dimension = get_object_or_404(Dimension, id=dimension_id)
    variable_id = dimension.variable
    return variable_id 
    
def criterion_answerinterview_value(criterion_id, user_id):
    criterion = get_object_or_404(MeasurementCriterion, id=criterion_id)
    if criterion:
        question = get_object_or_404(QuestionInterview, measurementCriterions=criterion)
        interview_id = question.interview
        if question:
            answer = AnswerInterview.objects.filter(questionInterview__interview_id=interview_id, user=user_id)
            if answer:
                criterion_value = answer.value
            return criterion_value

def calculate_criterion_interview(indicator_id, user_id):
    indicator=get_object_or_404(Indicator, id=indicator_id)
    criterions = MeasurementCriterion.objects.filter(indicator=indicator)
    indicator_value=0
    if criterions:
        criterions_value=0
        for criterion in criterions:
            criterions_value+=criterion_answerinterview_value(criterion.id, user_id)
        indicator_value = indicator.weigh * criterions_value
        return indicator_value
    return indicator_value

def calculate_indicator_interview(dimension_id, user_id):
    dimension=get_object_or_404(Dimension, id=dimension_id)
    indicators=Indicator.objects.filter(dimension=dimension)
    dimension_value=0
    if indicators:
        indicators_value=0
        for indicator in indicators:
            indicators_value+=calculate_criterion_interview(indicator.id, user_id)
        dimension_value = dimension.weigh * indicators_value
        return dimension_value
    return dimension_value

def calculate_variable_interview(variable_id, user_id):
    variable=get_object_or_404(Variable, id=variable_id)
    dimensions=Dimension.objects.filter(variable=variable)
    variable_value=0
    if dimensions:
        for dimension in dimensions:
            variable_value+=calculate_indicator_interview(dimension.id, user_id)
        return variable_value
    return variable_value

#Observation
def get_question_id_observation(answer_id):
    answer = get_object_or_404(ObservationResult, id=answer_id)
    if answer:
        question_id = answer.observationCriterions
        return question_id

def get_criterion_id_observation(question_id):
    question = get_object_or_404(ObservationCriterions, id=question_id)
    if question:
        criterion_id = question.measurementCriterions
        return criterion_id

def get_indicator_observation(criterion_id):
    citerion = get_object_or_404(MeasurementCriterion, id=criterion_id)
    if citerion:
        indicator_id = citerion.indicator
        return indicator_id 

def get_dimension_observation(indicator_id):
    indicator = get_object_or_404(Indicator, id=indicator_id)
    if indicator:
        dimension_id = indicator.dimension
        return dimension_id

def get_variable_observation(answer_id):
    question_id = get_question_id_observation(answer_id=answer_id)
    criterion_id = get_criterion_id_observation(question_id=question_id)
    indicator_id = get_indicator_observation(criterion_id=criterion_id)
    dimension_id = get_dimension_observation(indicator_id=indicator_id)
    dimension = get_object_or_404(Dimension, id=dimension_id)
    variable_id = dimension.variable
    return variable_id 
    
def criterion_answerobservation_value(criterion_id, user_id):
    criterion = get_object_or_404(MeasurementCriterion, id=criterion_id)
    if criterion:
        question = get_object_or_404(ObservationCriterions, measurementCriterions=criterion)
        observation_id = question.observation
        if question:
            answer = ObservationResult.objects.filter(observationCriterions__observation_id=observation_id, user=user_id)
            if answer:
                criterion_value = answer.value
            return criterion_value

def calculate_criterion_observation(indicator_id, user_id):
    indicator=get_object_or_404(Indicator, id=indicator_id)
    criterions = MeasurementCriterion.objects.filter(indicator=indicator)
    indicator_value=0
    if criterions:
        criterions_value=0
        for criterion in criterions:
            criterions_value+=criterion_answerobservation_value(criterion.id, user_id)
        indicator_value = indicator.weigh * criterions_value
        return indicator_value
    return indicator_value

def calculate_indicator_observation(dimension_id, user_id):
    dimension=get_object_or_404(Dimension, id=dimension_id)
    indicators=Indicator.objects.filter(dimension=dimension)
    dimension_value=0
    if indicators:
        indicators_value=0
        for indicator in indicators:
            indicators_value+=calculate_criterion_observation(indicator.id, user_id)
        dimension_value = dimension.weigh * indicators_value
        return dimension_value
    return dimension_value

def calculate_variable_observation(variable_id, user_id):
    variable=get_object_or_404(Variable, id=variable_id)
    dimensions=Dimension.objects.filter(variable=variable)
    variable_value=0
    if dimensions:
        for dimension in dimensions:
            variable_value+=calculate_indicator_observation(dimension.id, user_id)
        return variable_value
    return variable_value