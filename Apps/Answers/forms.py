from django import forms
from django.core.exceptions import ValidationError
from ..Instruments.models import *


class AnswerObservationReplyForm(forms.ModelForm):

    class Meta:
        model = ObservationResult
        fields = [
            'user',
        ]
        labels = {
            'user': 'Seleccione el Observado:',

        }
        widgets = {
            'user': forms.Select(
                attrs={
                    'class': 'form-control form-select',
                }),
        }
