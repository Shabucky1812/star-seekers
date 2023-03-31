from . import views
from django.urls import path

urlpatterns = [
    path('', views.events, name='events'),
    path('<slug:event_id>', views.event_details, name=('event_details'))
]
