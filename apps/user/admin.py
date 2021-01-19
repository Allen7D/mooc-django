from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.user.models import User as UserModel


# class UserAdmin(admin.ModelAdmin):
#     pass


admin.site.register(UserModel, UserAdmin)
