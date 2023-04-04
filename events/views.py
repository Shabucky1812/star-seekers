from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
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


@login_required
def add_event(request):

    template = 'event_form.html'

    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES)

        if event_form.is_valid():
            event = event_form.save()

            return redirect(
                reverse('event_details', kwargs={'event_id': event.id})
            )

    context = {
        'event_form': EventForm(),
        'submit_button_text': 'Add Event',
    }

    return render(request, template, context)


@login_required
def edit_event(request, event_id):

    template = 'event_form.html'

    event = get_object_or_404(Event, id=event_id)
    form = EventForm(instance=event)

    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES, instance=event)

        if event_form.is_valid():
            updated_event = event_form.save()

            return redirect(
                reverse('event_details', kwargs={'event_id': updated_event.id})
            )

    context = {
        'event_form': form,
        'submit_button_text': 'Edit Event',
    }

    return render(request, template, context)


@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()

    return redirect(reverse('events'))
