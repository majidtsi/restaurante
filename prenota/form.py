from django import forms
from django.contrib.auth.models import User

from prenota.models import Prenotazione, Piatti


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

class PrenotaForm(forms.ModelForm):
    class Meta:
        model = Prenotazione
        exclude = ('user',)
"""
class OrdineForm(forms.ModelForm):
    class Meta:
        model = Piatti
        fields = ['name' ,'description','category','price','ordini']

"""