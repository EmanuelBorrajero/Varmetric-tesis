from django import forms
from django.core.exceptions import ValidationError
from ..Instruments.models import *


class AnswerObservationReplyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get a list of users already in ObservationResult
        existing_users = ObservationResult.objects.values_list('user', flat=True)
        # Exclude those users from the queryset of the user field
        self.fields['user'].queryset = User.objects.exclude(id__in=existing_users)
        
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
