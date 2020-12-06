from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.utils.translation import gettext as _


from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None,{'fields':('email', 'password')} ), # each brakcet is a section, here we have 4 sections
        (_('Personal info'), {'fields':('name', )}),
        (
            _('Permissions'),
            {
                'fields':('is_active', 'is_staff', 'is_superuser')
            }
        ),
        (_('important dates'),{'fields':('last_login', )})
    )

    # User admin by default takes add_fieldsets to define fields which you
    # need for add page.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password','password2',)
        }),
    )

admin.site.register(models.User, UserAdmin)
