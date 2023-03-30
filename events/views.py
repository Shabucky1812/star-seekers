from django.shortcuts import render
from .models import Guide, Event


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
