from django.db import models
from .models import UserModel,Password
from django.contrib import admin

# Register your models here.
class PasswordAdmin(admin.StackedInline):
    model=Password
@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    inlines=[PasswordAdmin]
    class Meta:
        model=UserModel
@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    pass
