from django import forms
from django.core.exceptions import ValidationError
from ..Instruments.models import *


class AnswerObservationReplyForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in iter(self.fields):
    #         self.fields[field].widget.attrs.update({
    #             'class': 'form-control'
    #         })

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
