from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from captcha.fields import ReCaptchaField
from .models import User


class AuthenticationFormCapcha(AuthenticationForm):
    captcha = ReCaptchaField()

class UserRegistForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control m-1',
            'placeholder': 'Ingrese su contraseña...',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label='Confirmación de Contraseña*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control m-1',
            'placeholder': 'Confirme su contraseña...',
            'required': 'required',
        }
    ))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]
        labels = {
            'username': 'Nombre de Usuario*',
            'email': 'Correo Electrónico',
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control m-1',
                    'placeholder': 'Nombre de usuario...',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control m-1',
                    'placeholder': 'Correo electrónico...',
                }
            ),            
        }
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las Contraseñas no coinciden')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user