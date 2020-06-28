from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def impressum(request):
    return render(request, 'home/impressum.html')

def dsgvo(request):
    return render(request, 'home/dsgvo.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_name = form.cleaned_data['Name']
            from_email = form.cleaned_data['Email']
            message = form.cleaned_data['Nachricht']
            subject = 'Reservation'

            on_date = form.cleaned_data['Datum']
            on_time = form.cleaned_data['Uhrzeit']
            n_persons = form.cleaned_data['Personenanzahl']
            message += f'\nam {on_date}, um {on_time} Uhr für {n_persons} Personen.\nAbgeschickt von {from_name}'
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "home/contact.html", {'form': form})

def success(request):
    return render(request, "home/success.html")

