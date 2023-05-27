from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import Login

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', login_required(logout_then_login), name='logout'),
]