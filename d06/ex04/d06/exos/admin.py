from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from exos import models

# Register your models here.

class AUserAdmin(UserAdmin):
    pass

admin.site.register(models.AUser, UserAdmin)
