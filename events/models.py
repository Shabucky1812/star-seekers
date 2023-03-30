from django.db import models
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
