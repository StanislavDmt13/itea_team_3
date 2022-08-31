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


@admin.register(models.TrainProgram)
class ProgramAdmin(admin.ModelAdmin):

	ordering = ['id']
	list_display = ['name', 'author']
	fieldsets = ((None, {'fields': ('name', 'author', 'tasks')}),)

	add_fieldsets = (
		(None, {'classes': ('wide',),
				'fields': ('name', 'author', 'tasks')}),
	)


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):

	ordering = ['id']
	list_display = ['name', 'category']
	prepopulated_fields = {'slug': ('name',)}
	fieldsets = ((_('Task Info'), {'fields': ('name', 'description', 'category', 'example_photo', 'slug')}),)

	add_fieldsets = (
		(None, {'classes': ('wide',),
				'fields': ('name', 'description', 'category', 'example_photo', )}),
	)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ['name',]


@admin.register(models.Workouts)
class WorkoutsAdmin(admin.ModelAdmin):

	list_display = ['name_workout', ]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):

	list_display = ['question', ]