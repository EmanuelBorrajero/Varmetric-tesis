from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegistForm
from .models import User
#from .forms import AuthenticationFormCapcha


class Login(LoginView):
    #form_class = AuthenticationFormCapcha
    template_name = 'Login/login.html'

class RegistUser(CreateView):
    model = User
    form_class = UserRegistForm
    template_name = 'Login/regist.html'
    success_url = reverse_lazy('login')