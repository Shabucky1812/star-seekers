from django import forms
from .models import Event, Question


class EventForm(forms.ModelForm):
    """
    Form used to add and/or edit events from frontend
    """

    class Meta:
        model = Event
        fields = ('title', 'description', 'image', 'event_date', 'start_time',
                  'meet_point', 'expected_weather', 'guide')


class QuestionForm(forms.ModelForm):
    """
    Form used to upload questions about events from frontend
    """

    class Meta:
        model = Question
        fields = ('question_title', 'question_details')
