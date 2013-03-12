from django.shortcuts import render
from dynamic.models import *



from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    """This is the default/home page, it lists all of the
    apps in our database"""


    apps = App.objects.all()
    
    context = {"app_list":apps}
    
    return render(request, 'home.html', context)

def app_detail(request,slug):

    app = App.objects.get(slug=slug)
    context = {"app": app }

    return render(request, 'detail.html', context)
    
def del_app(request,slug):
    app = App.objects.get(slug=slug)
    app.delete()
    return HttpResponseRedirect('/?msg=app-deleted')


def app_form(request, slug=None):

    if slug == None:
        form = AppForm()
    else:
        app = App.objects.get(slug=slug)
        form = AppForm(instance=app)

    context = {"app": form }

    return render(request, 'app_form.html', context)



def save_app(request):

    form = AppForm(request.POST) # A form bound to the POST data

    form.save()

    #send them to the detail view after saving
    return HttpResponseRedirect('/app/{}'.format(form.slug))



