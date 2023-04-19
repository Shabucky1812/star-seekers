from django.test import TestCase
from django.contrib.auth.models import User
from .models import Event, Guide, Question, Answer


class TestModels(TestCase):
    """
    Tests for custom models
    """

    @classmethod
    def setUpTestData(self):
        """
        Initializes test user account and test data.
        """

        self.user = User.objects.create_superuser(username='test_user')
        self.user.set_password('test_password')
        self.user.save()

        self.guide = Guide.objects.create(name='Test Guide')

        self.event = Event.objects.create(
            title='Test Event',
            description='test description',
            event_date='2023-04-30',
            start_time='20:00',
            meet_point='test location',
            expected_weather=0,
            guide=self.guide
        )

        self.question = Question.objects.create(
            author=self.user,
            event=self.event,
            question_title='Test Question',
            question_details='Test details'
        )

        self.answer = Answer.objects.create(
            author=self.user,
            question=self.question,
            content='test answer'
        )

    def test_event_string_method(self):
        """
        Tests that the Event model's string method returns the expected value
        """

        self.assertEqual(str(self.event), 'Test Event')
