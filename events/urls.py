from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    EventListView, register_event, MyEventsListView, 
    OrganizerDashboardView, EventCreateView, EventUpdateView, EventDeleteView, custom_logout, cancel_registration
)

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('<int:event_id>/register/', register_event, name='register_event'),
    path('my-events/', MyEventsListView.as_view(), name='my_events'),
    path('my-events/<int:registration_id>/cancel/', cancel_registration, name='cancel_registration'),
    path('logout/', custom_logout, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='events/login.html'), name='login'),
    
    # URL per l'Organizzatore
    path('dashboard/', OrganizerDashboardView.as_view(), name='organizer_dashboard'),
    path('dashboard/new/', EventCreateView.as_view(), name='event_create'),
    path('dashboard/<int:pk>/edit/', EventUpdateView.as_view(), name='event_update'),
    path('dashboard/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
]