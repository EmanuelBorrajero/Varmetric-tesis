from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class UserAdmin(UserAdmin):
    readonly_fields = ['id']

admin.site.register(User, UserAdmin)