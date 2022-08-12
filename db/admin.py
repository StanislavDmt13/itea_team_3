from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from django.utils.translation import gettext as _


@admin.register(models.User)
class UserAdmin(BaseAdmin):
    ordering = ['id']
    list_display = ['email', 'username']


    fieldsets = (
            (None, {'fields': ('email', 'password')}),
        (
            _('Personal Info'),

                    {'fields': (
                        'avatar', 'username',
                        'first_name', 'last_name',
                        'birthday', 'phone',
                        'weight', 'height', 'country', 'city',)}),
		(
			_('Permissions'),

					{'fields': (
						'is_active',
		    			'is_staff',
		    			'is_superuser',
		    			'groups',
		    			'user_permissions')
            }
        ),
        (
			_('Important dates'),

					{'fields': (
						'last_login',
						 'created_at')
					}
		),
		)
    add_fieldsets = (
		(None, {'classes': ('wide',),
				'fields': ('email', 'username', 'password1', 'password2')}),
    	)

    readonly_fields = ('created_at',)
