from django import forms
from django.core.exceptions import ValidationError 
from ..Instruments.models import *

class AnswerPollReplyForm(forms.ModelForm):
    class Meta:
        model = AnswerPoll
        fields = [
            'answer',
        ]
        labels = {
            'answer': '',


        }
        widgets = {
            'answer': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Respuesta...',
                    }),

        }
    def clean_answer(self):
        answer = self.cleaned_data.get('answer')
        for char in answer:
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en la Respuesta')
        return answer

class AnswerInterviewReplyForm(forms.ModelForm):
    class Meta:
        model = AnswerInterview
        fields = [
            'answer',
        ]
        labels = {
            'answer': '',


        }
        widgets = {
            'answer': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Respuesta...',
                    }),

        }
    def clean_answer(self):
        answer = self.cleaned_data.get('answer')
        for char in answer:
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en la Respuesta')
        return answer

class AnswerObservationReplyForm(forms.ModelForm):
    class Meta:
        model = ObservationResult
        fields = [
            'value',
        ]
        labels = {
            'value': 'Puntuación:',


        }
        widgets = {
            'value': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Valor Obtenido...',
                    }),
        }