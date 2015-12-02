from django.contrib import admin

from .models import *

class UpdateAdmin(admin.ModelAdmin):

	"""Update Admin"""
	pass


admin.site.register(Student)
admin.site.register(School)
admin.site.register(Project)
admin.site.register(SchoolTeam)
admin.site.register(Employee)
admin.site.register(Update, UpdateAdmin)
admin.site.register(Administrator)

