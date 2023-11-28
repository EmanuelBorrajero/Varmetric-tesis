from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy

class IsStaffUserMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')