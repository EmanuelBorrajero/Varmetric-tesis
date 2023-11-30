from django import forms
from django.core.exceptions import ValidationError 
from .models import *

class VariableForm(forms.ModelForm):
    class Meta:
        model = Variable
        fields = [
            'name',
            'description',
            ]
        labels = {
            'name': 'Nombre*',
            'description': 'Descripción*',


        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la Variable...',
                    }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                    'placeholder': 'Ingrese una breve descripción',
                    }),
        }
    def clean_name(self):
        name = self.cleaned_data.get('name')
        for char in name:
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en el Nombre')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for char in description:
            if char in'`!@#$%^&*()_=+}{][></\|~':
                raise ValidationError('Caracteres incorrectos en la Descripción')
        return description

class DimensionForm(forms.ModelForm):
    class Meta:
        model = Dimension
        fields = [
            'name',
            'description',
            'weigh',
        ]
        labels = {
            'name': 'Nombre*',
            'description': 'Descripción*',
            'weigh': 'Peso*',


        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la Dimensión...',
                    }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                    'placeholder': 'Ingrese una breve descripción',
                    }),
            'weigh': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for char in name:
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en el Nombre')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for char in description:
            if char in'`!@#$%^&*()_=+}{][><\|~':
                raise ValidationError('Caracteres incorrectos en la Descripción')
        return description

    def clean_weigh(self):
        weigh = self.cleaned_data.get('weigh')
        if weigh < 0:
            raise ValidationError('El peso no puede ser un número negativo')
        return weigh

class IndicatorForm(forms.ModelForm):
    class Meta:
        model = Indicator
        fields = [
            'name',
            'description',
            'weigh',
        ]
        labels = {
            'name': 'Nombre*',
            'description': 'Descripción*',
            'weigh': 'Peso*',


        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del Indicador...',
                    }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                    'placeholder': 'Ingrese una breve descripción',
                    }),
            'weigh': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for char in name:
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en el Nombre')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for char in description:
            if char in'`!@#$%^&*()_=+}{][><\|~':
                raise ValidationError('Caracteres incorrectos en la Descripción')
        return description

    def clean_weigh(self):
        weigh = self.cleaned_data.get('weigh')
        if weigh < 0:
            raise ValidationError('El peso no puede ser un número negativo')
        return weigh

class MeasurementCriterionForm(forms.ModelForm):
    class Meta:
        model = MeasurementCriterion
        exclude=('indicator',)
        labels = {
            'name': 'Nombre*',
            'description': 'Descripción*',
            'min_value': 'Valor Minimo*',
            'max_value': 'Valor Máximo*',


        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del Criterio de Medida...',
                    }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                    'placeholder': 'Ingrese una breve descripción',
                    }),
            'min_value': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    }),
            'max_value': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for char in name:
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en el Nombre')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for char in description:
            if char in'`!@#$%^&*()_=+}{][><\|~':
                raise ValidationError('Caracteres incorrectos en la Descripción')
        return description

    def clean_min_value(self):
            min_value = self.cleaned_data.get('min_value')
            if min_value < 0:
                raise ValidationError('El valor minimo no puede ser un número negativo')
            return min_value

    def clean_max_value(self):
        max_value = self.cleaned_data.get('max_value')
        if max_value < 0:
            raise ValidationError('El valor máximo no puede ser un número negativo')
        return max_value
    

class ScaleForm(forms.ModelForm):
    class Meta:
        model = Scale
        fields = [
            'scale_label',
            ]
        labels = {
            'scale_label': 'Etiqueta Lingüística*',
        }
        widgets = {
            'scale_label': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Etiqueta Lingüística...',
                    }),
        }
    def clean_scale_label(self):
        scale_label = self.cleaned_data.get('scale_label')
        for char in scale_label:
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en la Etiqueta Lingüística')
        return scale_label