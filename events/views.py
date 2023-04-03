from django.shortcuts import render, get_object_or_404
from .models import Guide, Event
from .forms import EventForm


def index(request):

    template = 'index.html'

    return render(request, template)


def events(request):

    upcoming_events = Event.objects.all()

    template = 'events.html'
    context = {
        'events': upcoming_events
    }

    return render(request, template, context)


def event_details(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    template = 'event_details.html'
    context = {
        'event': event
    }

    return render(request, template, context)


def add_event(request):

    template = 'add_event.html'
    context = {
        'event_form': EventForm()
    }

    return render(request, template, context)
