from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput

class ContactForm(forms.Form):
    Name = forms.CharField(required=True, max_length=100)
    Email = forms.EmailField(required=True)
    Telefon = forms.IntegerField(required=False)
    Nachricht = forms.CharField(widget=forms.Textarea, required=False)
    # Datum_und_Uhrzeit = forms.DateTimeField(widget=DateTimePickerInput(format='%d/%m/%Y HH:mm'))
    Datum = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    Uhrzeit = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}))

    # Uhrzeit = forms.TimeField(widget=TimePickerInput(format='HH:mm'))
    Personenanzahl = forms.IntegerField(min_value=1, max_value=100)