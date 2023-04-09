from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone
from .models import Guide, Event, Question
from .forms import EventForm, QuestionForm


def index(request):

    template = 'index.html'

    context = {
        'page_title': 'Home'
    }

    return render(request, template, context)


def events(request):

    today = timezone.now()
    upcoming_events = Event.objects.filter(event_date__gte=today)

    template = 'events.html'
    context = {
        'events': upcoming_events,
        'page_title': 'Events'
    }

    return render(request, template, context)


def event_detail(request, event_id):

    event = get_object_or_404(Event, id=event_id)
    try:
        event_questions = Question.objects.filter(event=event)
    except Question.DoesNotExist:
        event_questions = None

    template = 'event_detail.html'
    question_form = QuestionForm()

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author = request.user
            question.event = event
            question.save()

            return redirect(
                reverse('event_detail', kwargs={'event_id': event.id})
            )

    context = {
        'question_form': question_form,
        'event': event,
        'asked_questions': event_questions,
        'page_title': f'{event.title}'
    }

    return render(request, template, context)


@staff_member_required
def add_event(request):

    template = 'event_form.html'
    event_form = EventForm()

    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES)

        if event_form.is_valid():
            event = event_form.save()

            return redirect(
                reverse('event_detail', kwargs={'event_id': event.id})
            )

    context = {
        'event_form': event_form,
        'submit_button_text': 'Add Event',
        'page_title': 'New Event'
    }

    return render(request, template, context)


@staff_member_required
def edit_event(request, event_id):

    template = 'event_form.html'

    event = get_object_or_404(Event, id=event_id)
    event_form = EventForm(instance=event)

    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES, instance=event)

        if event_form.is_valid():
            updated_event = event_form.save()

            return redirect(
                reverse('event_detail', kwargs={'event_id': updated_event.id})
            )

    context = {
        'event_form': event_form,
        'submit_button_text': 'Save Changes',
        'page_title': f'Editing Event: {event.title}'
    }

    return render(request, template, context)


@staff_member_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()

    return redirect(reverse('events'))
