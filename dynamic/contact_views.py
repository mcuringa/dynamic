from django.shortcuts import render
from dynamic.models import *

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse, HttpResponseRedirect

from django.core.mail import send_mail, BadHeaderError

from datetime import datetime

def contact(request):
    
    admin_email = "mcuringa@adelphi.edu"

    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass

            # add a header to the subject, to make it easier to sort/find
            # in email client
            subject = "[Apps4Ed Contact] {}".format(form.cleaned_data["subject"])
            
            # add the sender's name and current time to the body
            # of the email
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = """From: {}
Time Received: {}
Phone: {}
Message:
{}""".format(form.cleaned_data["from_name"], now, form.cleaned_data["phone"], form.cleaned_data["message"])
            
            #try to send it
            try:
                send_mail(subject, message, form.cleaned_data["from_email"], [admin_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            messages.add_message(request, messages.INFO, "Thank you for contacting us!")
            return HttpResponseRedirect('/')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form,})

