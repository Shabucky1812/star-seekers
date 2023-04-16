from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Guide, Event


class TestViews(TestCase):
    """
    Tests views functionality and that all views render the correct templates.
    """

    @classmethod
    def setUpTestData(self):
        """
        Initializes test user account and test data.
        """

        self.user = User.objects.create(username='test_user')
        self.user.set_password('test_password')
        self.user.save()

        self.guide = Guide.objects.create(name='Test Guide')

        self.event = Event.objects.create(
            title='Test Event',
            event_date='2023-04-30',
            start_time='20:00',
            guide=self.guide
        )

    def test_get_home_page(self):
        """
        Tests that the home page is retrieved correctly,
        using the index.html template
        """

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_events_page(self):
        """
        Tests that the events page is retrieved correctly,
        using the events.html template
        """

        response = self.client.get(reverse('events', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events.html')
