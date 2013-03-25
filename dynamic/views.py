from django.shortcuts import render
from dynamic.models import *

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse, HttpResponseRedirect


def register(request):
    
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Your account is created, welcome to Apps4Ed.')

            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.INFO, 'There was a problem creating your account.')
    
    context = {"form": form}

    return render(request, 'register.html', context)

def user_login(request):
    
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.INFO, 'You are successfully logged in.')
            return HttpResponseRedirect('/')

        return HttpResponseRedirect('/login-sorry')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'You are now logged out.')
    return HttpResponseRedirect('/')


def login_error(request):
    """Let the user know that login failed."""

    return render(request, 'login-sorry.html')

def index(request):
    """This is the default/home page, it lists all of the
    apps in our database"""

    apps = App.objects.all()
    
    context = {"app_list": apps}
    
    return render(request, 'home.html', context)

def app_detail(request,pk):

    app = App.objects.get(pk=pk)
    context = {"app": app }

    return render(request, 'detail.html', context)
    
def del_app(request, pk):
    """Delete an app from the database."""
    
    messages.add_message(request, messages.INFO, "'{}' deleted.".format(app.title))
    app.delete()
    return HttpResponseRedirect('/')


def app_form(request, pk=0):
    """Create a form to edit an existing app or create a new app"""

    if pk == 0:
        form = AppForm()
    else:
        app = App.objects.get(pk=pk)
        form = AppForm(instance=app)

    context = { "app": form, "pk": pk }

    return render(request, 'app_form.html', context)

def save_app(request):

    pk = int(request.POST["id"])
    if pk == 0:
        # read the form POST data into our AppForm object
        form = AppForm(request.POST)
    else:
        app = App.objects.get(pk=pk)
        form = AppForm(request.POST, instance=app)

    app = form.save()

    #send them to the detail view after saving
    return HttpResponseRedirect("/")

def rate_app(request, pk, rating):
    """Add a new rating for this app."""
    
    app = App.objects.get(pk=pk)
    
    # note all parameters from urls come in as strings, we 
    # need to make our rating an int
    app.rate(int(rating))
    app.save()

    #send them to the detail view after saving
    return HttpResponseRedirect("/")


