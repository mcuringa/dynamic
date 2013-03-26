from django.shortcuts import render
from dynamic.models import *

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse, HttpResponseRedirect

def app_list(request):
    """This is the default/home page, it lists all of the
    apps in our database"""

    apps = App.objects.all()
    
    context = {"app_list": apps}
    
    return render(request, 'home.html', context)

def app_detail(request,pk):

    app = App.objects.get(pk=pk)
    reviews = Review.objects.filter(app__id=pk)
    context = {"app": app, "reviews": reviews }

    return render(request, 'detail.html', context)
    
def del_app(request, pk):
    """Delete an app from the database."""
    
    app = App.objects.get(pk=pk)    
    messages.add_message(request, messages.INFO, "'{}' deleted.".format(app.title))
    app.delete()
    return HttpResponseRedirect('/')


def app_form(request, pk=0):
    """Create a form to edit an existing app or create a new app"""

    print("calling app_form()")

    # if the user isn't signed in, send them to the login screen
    if not request.user.is_authenticated():
        messages.add_message(request, messages.INFO, "You mussed be logged in to add an App")
        return HttpResponseRedirect('/login')

    if pk == 0:
        form = AppForm()
    else:
        app = App.objects.get(pk=pk)
        form = AppForm(instance=app)

    context = { "app": form, "pk": pk }

    print(form)

    return render(request, 'app_form.html', context)

def save_app(request):

    pk = int(request.POST["id"])
    
    # the current logged in user
    user = request.user
    
    # if the user isn't signed in, send them to the login screen
    if not user.is_authenticated():
        messages.add_message(request, messages.INFO, "You mussed be logged in to add an App")

        return HttpResponseRedirect('/login')
    
    # this is if we are creating a new App
    if pk == 0:
        # read the form POST data into our AppForm object
        form = AppForm(request.POST)
        # set the creator (only once) to the current logged in user
        form.instance.creator = user
    
    # this is if we are updating an existing app
    else:
        app = App.objects.get(pk=pk)
        form = AppForm(request.POST, instance=app)

    form.instance.modifier = user
    
    app = form.save()

    #send them to the detail view after saving
    return HttpResponseRedirect("/")
