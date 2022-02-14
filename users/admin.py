from django.contrib import admin
from users.models import App_User
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class App_UserInline(admin.StackedInline):
    model = App_User
    can_delete = False
    verbose_name_plural = 'App_Users'

class CustomisedUserAdmin(UserAdmin):
    inlines = (App_UserInline, )

admin.site.unregister(User)
admin.site.register(User, CustomisedUserAdmin)