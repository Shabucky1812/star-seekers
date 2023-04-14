from django.contrib import admin
from .models import Guide, Event, Question, Answer


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    """
    Initializes the guide model for the admin panel.

    Displays the guide's name and role in the list display.
    """

    list_display = ('name', 'role')
    search_fields = ['name']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Initializes the event model for the admin panel.

    Displays the event title, guide, date, and start time in the list display.
    Events are filterable by date and time.
    """

    list_display = ('title', 'guide', 'event_date', 'start_time')
    list_filter = ('event_date', 'start_time')
    search_fields = ['title']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Initializes the quesion model for the admin panel.

    Displays the question's author, related event, title, and
    upload time in the list display.
    Questions are filterable by upload time.
    """

    list_display = ('author', 'event', 'question_title', 'uploaded_on')
    list_filter = ('uploaded_on',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """
    Initializes the answer model for the admin panel.

    Displays the answer's author and related question in the list display.
    """

    list_display = ('author', 'question')
