from django.test import TestCase
from .forms import EventForm, QuestionForm


class TestEventForm(TestCase):
    """
    Tests for the fields of the Event Form
    """

    def test_event_title_is_required(self):
        """
        Tests that the event's title field is required
        """

        form = EventForm({'title': ''})
        self.assertFalse(form.is_valid())
