"""AprendizajeCreativo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name= 'index' ),
    path('administración/', login_required(Admin.as_view()), name= 'adminsite' ),
    path('metricas/', include(('Apps.Metrics.urls', 'Metrics'))),
    path('instrumentos/', include(('Apps.Instruments.urls', 'Instruments'))),
    path('respuestas/', include(('Apps.Answers.urls', 'Answers'))),
    path('accounts/', include('Apps.AccesControl.urls'), name='accounts'),
]
