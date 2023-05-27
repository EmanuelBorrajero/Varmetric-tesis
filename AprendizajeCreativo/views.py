from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'index.html'

class Admin(TemplateView):
    template_name = 'admin.html'