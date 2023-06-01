from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import ReCaptchaField


class AuthenticationFormCapcha(AuthenticationForm):
    captcha = ReCaptchaField()