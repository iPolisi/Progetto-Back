from django import forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Event, Registration
from django.contrib.auth import logout

# Vista che mostra la lista degli eventi
class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

#Iscrizione ad un evento (previo login)
@login_required
def register_event(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, id=event_id)
        
        # Controllo se l'utente è già iscritto per evitare doppioni
        iscrizione_esistente = Registration.objects.filter(attendee=request.user, event=event).exists()
        
        if not iscrizione_esistente:
            # Aggiunta nel database
            Registration.objects.create(attendee=request.user, event=event)
            messages.success(request, f"Ti sei iscritto con successo a: {event.title}!")
        else:
            messages.warning(request, "Sei già iscritto a questo evento!")
            
    return redirect('event_list')

# Vista per vedere "I Miei Eventi"
class MyEventsListView(LoginRequiredMixin, ListView):
    model = Registration
    template_name = 'events/my_events.html'
    context_object_name = 'registrations'

    #Faccio vedere solo gli eventi a cui l'utente è iscritto
    def get_queryset(self):
        return Registration.objects.filter(attendee=self.request.user)


#Logica per il pannello dell'organizzatore

# 1Entra solo chi è in Organizer
class OrganizerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Organizer').exists() or self.request.user.is_superuser

# 2 Dashboard (Lista dei propri eventi)
class OrganizerDashboardView(LoginRequiredMixin, OrganizerRequiredMixin, ListView):
    model = Event
    template_name = 'events/organizer_dashboard.html'
    context_object_name = 'events'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Event.objects.all().order_by('-date')
        return Event.objects.filter(organizer=self.request.user).order_by('-date')

# 3Pagina per Creare un evento
class EventCreateView(LoginRequiredMixin, OrganizerRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'description', 'date']
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('organizer_dashboard')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
        form.fields['title'].widget.attrs.update({'class': 'form-control'})
        form.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 3})
        return form

    def form_valid(self, form):
        form.instance.organizer = self.request.user # Imposta chi lo ha creato
        messages.success(self.request, "Evento creato con successo!")
        return super().form_valid(form)

# 4 Pagina per Modificare un evento
class EventUpdateView(LoginRequiredMixin, OrganizerRequiredMixin, UpdateView):
    model = Event
    fields = ['title', 'description', 'date']
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('organizer_dashboard')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
        form.fields['title'].widget.attrs.update({'class': 'form-control'})
        form.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 3})
        return form

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Event.objects.all()
        return Event.objects.filter(organizer=self.request.user)

# 5Pagina per Eliminare un evento
class EventDeleteView(LoginRequiredMixin, OrganizerRequiredMixin, DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('organizer_dashboard')

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Event.objects.all()
        return Event.objects.filter(organizer=self.request.user)
    

def custom_logout(request):
    logout(request)
    messages.info(request, "Ti sei disconnesso con successo.")
    return redirect('event_list')


@login_required
def cancel_registration(request, registration_id):
    if request.method == 'POST':
        # Cerca l'iscrizione, assicurandosi che appartenga all'utente che ha fatto il login
        reg = get_object_or_404(Registration, id=registration_id, attendee=request.user)
        titolo_evento = reg.event.title
        reg.delete() # Elimina l'iscrizione
        messages.success(request, f"Iscrizione a '{titolo_evento}' annullata con successo.")
    return redirect('my_events')