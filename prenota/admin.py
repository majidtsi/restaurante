from django.contrib import admin
from .models import Piatti,Prenotazione,Ordini

# Register your models here.
admin.site.register(Prenotazione)
admin.site.register(Piatti)
admin.site.register(Ordini)
