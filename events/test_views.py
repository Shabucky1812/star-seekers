from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Guide, Event, Question, Answer


class TestViews(TestCase):
    """
    Tests views functionality and that all views render the correct templates.
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
            event_date='2023-04-30',
            start_time='20:00',
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

        response = self.client.get(reverse('events', args=[10]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events.html')

    def test_get_event_detail_page(self):
        """
        Tests that the event detail page is retrieved correctly,
        using the event_detail.html template
        """

        response = self.client.get(reverse('event_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event_detail.html')

    def test_get_add_event_page(self):
        """
        Tests that the add event page is retrieved correctly,
        using the event_form.html template
        """

        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/events/add_event/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event_form.html')

    def test_get_edit_event_page(self):
        """
        Tests that the edit event page is retrieved correctly,
        using the event_form.html template
        """

        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('edit_event', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'event_form.html')

    def test_delete_event(self):
        """
        Tests that the delete_event view functions correctly and
        redirects the user to the home page.
        """

        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('delete_event', args=[1]))
        self.assertRedirects(response, '/')
        events = Event.objects.filter(id=self.event.id)
        self.assertEqual(len(events), 0)
