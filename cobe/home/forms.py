from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class ContactForm(forms.Form):
    Name = forms.CharField(required=True, max_length=100)
    Email = forms.EmailField(required=True)
    Telefon = forms.IntegerField()
    Nachricht = forms.CharField(widget=forms.Textarea, required=True)
    Datum = forms.DateField(widget=forms.SelectDateWidget)
    Uhrzeit = forms.TimeField()
    Personenanzahl = forms.IntegerField(min_value=1, max_value=100)