from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    #Variable url
    path('listado/variables/', login_required(VariableLIst.as_view()), name='variable_list'),
    path('crear/variable/', login_required(VariableCreate.as_view()), name='variable_create'),
    path('editar/variable/<pk>', login_required(VariableUpdate.as_view()), name='variable_update'),
    path('eliminar/variable/<pk>', login_required(VariableDelete.as_view()), name='variable_delete'),
    path('detalles/variable/<pk>', login_required(VariableDetail.as_view()), name='variable_detail'),

    #Dimension
    path('listado/dimensiones/<pk>', login_required(DimensionLIst.as_view()), name='dimension_list'),
    path('crear/dimensión/<pk>', login_required(DimensionCreate.as_view()), name='dimension_create'),
    path('editar/dimensión/<pk>', login_required(DimensionUpdate.as_view()), name='dimension_update'),
    path('eliminar/dimensión/<pk>', login_required(DimensionDelete.as_view()), name='dimension_delete'),
    path('detalles/dimensión/<pk>', login_required(DimensionDetail.as_view()), name='dimension_detail'),

    #Indicator
    path('listado/indicador/<pk>', login_required(IndicatorLIst.as_view()), name='indicator_list'),
    path('crear/indicador/<pk>', login_required(IndicatorCreate.as_view()), name='indicator_create'),
    path('detalles/indicador/<pk>', login_required(IndicatorDetail.as_view()), name='indicator_detail'),

    #Measurement Criterion
    path('listado/criterio de medida/<pk>', login_required(MeasurementCriterionLIst.as_view()), name='measurement_criterion_list'),
    path('crear/criterio de medida/<pk>', login_required(MeasurementCriterionCreate.as_view()), name='measurement_criterion_create'),
]