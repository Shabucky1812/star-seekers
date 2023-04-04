from . import views
from django.urls import path

urlpatterns = [
    path('', views.events, name='events'),
    path('<slug:event_id>', views.event_details, name='event_details'),
    path('add_event/', views.add_event, name='add_event'),
    path('edit_event/<slug:event_id>/', views.edit_event, name='edit_event'),
    path('delete_event/<slug:event_id>/', views.delete_event, name='delete_event'),
]
