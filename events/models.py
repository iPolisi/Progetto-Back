from django.db import models
from django.contrib.auth.models import User

# Tabella degli Eventi
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    #Relazione tra tabelle, che collega l'evento all'utente creatore
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')

    def __str__(self):
        return self.title

# Tabella delle Iscrizioni agli eventi
class Registration(models.Model):
    attendee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.attendee.username} iscritto a {self.event.title}"