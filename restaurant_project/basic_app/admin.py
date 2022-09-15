from django.contrib import admin
from . import models

class UserRegistrationAdmin(admin.ModelAdmin):
    search_fields = ('user__username', 'branch', 'year', )

admin.site.register(models.UserRegistration, UserRegistrationAdmin)

