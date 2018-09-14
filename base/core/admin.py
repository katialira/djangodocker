from django.contrib import admin

# Register your models here.
from .models import Human, Talks

@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
	list_display = ( 'user', 'current', 'lightning', 'is_active')

@admin.register(Talks)
class TalksAdmin(admin.ModelAdmin):
	list_display = ( 'human', 'name', 'date')
