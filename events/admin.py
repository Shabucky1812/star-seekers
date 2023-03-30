from django.contrib import admin
from .models import Guide, Event


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):

    list_display = ('name', 'role')
    search_fields = ['name']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ('title', 'guide', 'event_date', 'start_time')
    list_filter = ('event_date', 'start_time')
    search_fields = ['title']
