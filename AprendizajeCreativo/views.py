from django.views.generic import TemplateView
from .mixins import IsStaffUserMixin

class Index(TemplateView):
    template_name = 'index.html'

class Admin(IsStaffUserMixin, TemplateView):
    template_name = 'admin.html'