from django.shortcuts import render
from dynamic.models import *



from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    """This is the default/home page, for now it is just a string written
    right in the view method."""


    apps = App.objects.all()
    
    context = {"app_list":apps}
    
    return render(request, 'home.html', context)

def detail(request,slug):

    app = App.objects.get(slug=slug)
    context = {"app": app }

    return render(request, 'detail.html', context)
    
def delete(request,slug):
    app = App.objects.get(slug=slug)
    app.delete()
    return HttpResponseRedirect('/?msg=app-deleted')


def app_form(request):
    
    app = AppForm()

    context = {"app": app }

    return render(request, 'app_form.html', context)



def save_app(request):

    form = AppForm(request.POST) # A form bound to the POST data

    form.save()
    
    return HttpResponseRedirect('/')



