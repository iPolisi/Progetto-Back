from django.contrib import admin
from .models import Event, Registration

#Tabelle ammenate al pannello di amministrazione di Django
admin.site.register(Event)
admin.site.register(Registration)