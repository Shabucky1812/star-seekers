from django.contrib import admin
from .models import Guide, Event, Question, Answer


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):

    list_display = ('name', 'role')
    search_fields = ['name']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ('title', 'guide', 'event_date', 'start_time')
    list_filter = ('event_date', 'start_time')
    search_fields = ['title']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = ('author', 'event', 'uploaded_on')
    list_filter = ('uploaded_on',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    list_display = ('author', 'question')
