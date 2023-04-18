from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage
from .models import Guide, Event, Question, Answer
from .forms import EventForm, QuestionForm


def index(request):
    """
    Renders home page using index.html.

    Passes 'Home' as the page title in context.
    """

    template = 'index.html'

    context = {
        'page_title': 'Home'
    }

    return render(request, template, context)


def events(request, page=1):
    """
    Renders events page using events.html.

    Passes upcoming events as 'events' and 'Events' as the page title
    in context.
    Uses Paginator to return 6 events per page.
    """

    today = timezone.now()
    upcoming_events = Event.objects.filter(event_date__gte=today)
    paginator = Paginator(upcoming_events, 6)

    try:
        upcoming_events = paginator.page(page)
    except EmptyPage:
        upcoming_events = paginator.page(paginator.num_pages)

    template = 'events.html'
    context = {
        'events': upcoming_events,
        'page_title': 'Events'
    }

    return render(request, template, context)


def event_detail(request, event_id):
    """
    Renders event details page using event_detail.html.

    Passes to context:
    - question form from forms.py as 'question_form'
    - relevant event as 'event'
    - questions about the event (if any) as 'asked_questions'
    - relevant question answers (if any) as 'answers'
    - the event's title as the page title.

    If a post request is made from a user submitting a question
    then the view receives the form data and adds the author and event
    info to the question before saving it to the db and redirecting the user
    back to the same page.
    """

    event = get_object_or_404(Event, id=event_id)
    event_questions = Question.objects.filter(event=event)

    answers = []
    if event_questions:
        for question in event_questions:

            answer = Answer.objects.filter(question=question)

            if answer:
                answers.append(answer[0])

    template = 'event_detail.html'
    question_form = QuestionForm()

    if request.method == 'POST' and request.user.is_authenticated:
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
        'answers': answers,
        'page_title': f'{event.title}',
    }

    return render(request, template, context)


@staff_member_required
def add_event(request):
    """
    Renders add event form using event_form.html. Only accessible to admins.

    Passes to context:
    - The empty event form from forms.py as 'event_form'
    - 'Add Event' as the submit button text
    - 'New Event' as the page title.

    If a post request is made from the user attempting to create an event
    then the view receives and validates the form data before saving it to
    the db as a new Event instance. The user is redirected to the new event's
    detail page.
    """

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
    """
    Renders edit event from using event_form.html. Only accessible to admins.

    Passes to context:
    - The pre-filled event form using event info as 'event_form'
    - 'Save Changes' as the submit button text
    - 'Editing Event: (relevant event title)' as the page title

    If a post request is made from the user attempting to save their event
    changes then the view receives and validates the form data before updating
    the existing event info. The user is redirected to the changed event's
    detail page.
    """

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
    """
    Deletes the event associated with the request. Only accessible to admins.

    Redirects user to the home page.
    """
    event = get_object_or_404(Event, id=event_id)
    event.delete()

    return redirect(reverse('home'))


def handler403(request, exception):
    """
    Render custom 403 template instead of default.
    """

    return render(request, '403.html', status=403)


def handler404(request, exception):
    """
    Render custom 404 template instead of default.
    """

    return render(request, '404.html', status=404)


def handler405(request, exception):
    """
    Render custom 405 template instead of default.
    """

    return render(request, '405.html', status=405)


def handler500(request):
    """
    Render custom 500 template instead of default.
    """

    return render(request, '500.html', status=500)
