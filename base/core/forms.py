from django import forms
from .models import Talks

class TalksForm(forms.ModelForm):

   class Meta:
     model = Talks
     fields = ('human','name', 'link', 'cicle')