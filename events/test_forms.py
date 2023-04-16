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
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_event_description_is_required(self):
        """
        Tests that the event's description field is required
        """

        form = EventForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_event_date_is_required(self):
        """
        Tests that the event's event_date field is required
        """

        form = EventForm({'event_date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('event_date', form.errors.keys())
        self.assertEqual(form.errors['event_date'][0], 'This field is required.')

    def test_event_start_time_is_required(self):
        """
        Tests that the event's start_time field is required
        """

        form = EventForm({'start_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('start_time', form.errors.keys())
        self.assertEqual(form.errors['start_time'][0], 'This field is required.')

    def test_event_meet_point_is_required(self):
        """
        Tests that the event's meet_point field is required
        """

        form = EventForm({'meet_point': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('meet_point', form.errors.keys())
        self.assertEqual(form.errors['meet_point'][0], 'This field is required.')
