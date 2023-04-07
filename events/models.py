from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

WEATHER_OPTIONS = ((0, 'Unknown'), (1, 'Clear'), (2, 'Chilly'), (3, 'Rainy'), (4, 'Snowy'), (5, 'Stormy'))
GUIDE_ROLES = ((0, 'Junior Seeker'), (1, 'Senior Seeker'), (3, 'Guest Seeker'))


class Guide(models.Model):
    name = models.CharField(max_length=50)
    role = models.IntegerField(choices=GUIDE_ROLES, default=0)
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=600)
    image = CloudinaryField('image', default='placeholder')
    event_date = models.DateField()
    start_time = models.TimeField()
    meet_point = models.CharField(max_length=100)
    expected_weather = models.IntegerField(choices=WEATHER_OPTIONS, default=0)
    guide = models.ForeignKey(Guide, on_delete=models.RESTRICT, related_name='events')

    class Meta:
        ordering = ['event_date', 'start_time']

    def __str__(self):
        return self.title


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='question')
    question_title = models.CharField(max_length=100)
    question_details = models.TextField(max_length=600)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['uploaded_on']

    def __str__(self):
        return f'Question by {self.author} about {self.event}: {self.question_title}'


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer')
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='answer')
    content = models.TextField(max_length=600)
    answered_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['question']

    def __str__(self):
        return f'Answer for Question: {self.question.question_title}'
