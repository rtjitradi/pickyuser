from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # https://docs.djangoproject.com/en/3.1/topics/auth/customizing/

from pickyuser_app.models import CustomUserMod
from pickyuser_app.forms import AdminForm


# Register your models here.
# https://stackoverflow.com/questions/15012235/using-django-auth-useradmin-for-a-custom-user-model
class CustomizedUserAdmin(UserAdmin):
    model = CustomUserMod

    fieldsets = UserAdmin.fieldsets + (
        ('Admin Custom Fields', {'fields': ('display_name', 'age', 'homepage',)}),
    )


admin.site.register(CustomUserMod, CustomizedUserAdmin)
