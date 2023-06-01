from django.contrib.auth.views import LoginView
#from .forms import AuthenticationFormCapcha


class Login(LoginView):
    #form_class = AuthenticationFormCapcha
    template_name = 'Login/login.html'

