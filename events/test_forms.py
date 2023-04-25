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
        self.assertEqual(form.errors['description'][0],
                         'This field is required.')

    def test_event_date_is_required(self):
        """
        Tests that the event's event_date field is required
        """

        form = EventForm({'event_date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('event_date', form.errors.keys())
        self.assertEqual(form.errors['event_date'][0],
                         'This field is required.')

    def test_event_start_time_is_required(self):
        """
        Tests that the event's start_time field is required
        """

        form = EventForm({'start_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('start_time', form.errors.keys())
        self.assertEqual(form.errors['start_time'][0],
                         'This field is required.')

    def test_event_meet_point_is_required(self):
        """
        Tests that the event's meet_point field is required
        """

        form = EventForm({'meet_point': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('meet_point', form.errors.keys())
        self.assertEqual(form.errors['meet_point'][0],
                         'This field is required.')

    def test_event_guide_is_required(self):
        """
        Tests that the event's guide field is required
        """

        form = EventForm({'guide': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('guide', form.errors.keys())
        self.assertEqual(form.errors['guide'][0], 'This field is required.')

    def test_fields_are_explicit_in_event_metaclass(self):
        """
        Tests that fields are explicit in event metaclass
        """

        form = EventForm()
        self.assertEqual(form.Meta.fields, ('title', 'description', 'image',
                                            'event_date', 'start_time',
                                            'meet_point', 'expected_weather',
                                            'guide'))


class TestQuestionForm(TestCase):
    """
    Tests for the fields of the Question Form
    """

    def test_question_title_is_required(self):
        """
        Tests that the question's title field is required
        """

        form = QuestionForm({'question_title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('question_title', form.errors.keys())
        self.assertEqual(form.errors['question_title'][0],
                         'This field is required.')

    def test_question_details_is_required(self):
        """
        Tests that the question's details field is required
        """

        form = QuestionForm({'question_details': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('question_details', form.errors.keys())
        self.assertEqual(form.errors['question_details'][0],
                         'This field is required.')

    def test_fields_are_explicit_in_question_metaclass(self):
        """
        Tests that fields are explicit in question metaclass
        """

        form = QuestionForm()
        self.assertEqual(form.Meta.fields, ('question_title',
                                            'question_details'))
