from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'image', 'event_date', 'start_time', 'meet_point', 'expected_weather', 'guide')
