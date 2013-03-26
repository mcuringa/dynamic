from django.shortcuts import render
from dynamic.models import *

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

def review(request, app_id):
    """Create the form to Review an App"""

    # if the user isn't signed in, send them to the login screen
    if not request.user.is_authenticated():
        messages.add_message(request, messages.INFO, "You mussed be logged in to add a review.")
        return HttpResponseRedirect('/login')

    app = App.objects.get(pk=int(app_id))
    # check to see if the user has already reviewed this App
    try:
        review = Review.objects.get(app__id=app.id, reviewer__id=request.user.id)
        form = ReviewForm(instance = review)
        pk = review.id
    except:
        form = ReviewForm()
        pk = 0

    form.instance.app = app
    form.instance.reviewer = request.user
    context = { "review": form, "pk": pk, "app_id": app_id }

    return render(request, 'review_form.html', context)

def save_review(request):
    """Save a review for an App and update the rating for the App"""

    pk = int(request.POST["id"])
    
    # the current logged in user
    user = request.user

    # if the user isn't signed in, send them to the login screen
    if not user.is_authenticated():
        messages.add_message(request, messages.INFO, "You must be logged in to review an App")
        return HttpResponseRedirect('/login')

    # I don't know why DJango isn't reading this correctly
    rating = int(request.POST["rating"])
    app = App.objects.get(pk=int(request.POST["app_id"]))

    # this is if we are creating a new Review
    if pk == 0:
        form = ReviewForm(request.POST)
    # this is if we are updating an existing Review
    else:
        review = Review.objects.get(pk=pk)
        form = ReviewForm(request.POST, instance=review)
    
    # set the rating, user, and app for this review
    form.instance.rating = rating
    form.instance.reviewer = user
    form.instance.app = app     
    review = form.save()

    messages.add_message(request, messages.INFO, "Your review has been added.")

    #send them to the detail view after saving
    return HttpResponseRedirect("/app/{}".format(app.id))


def rate_app(request, pk, rating):
    """Add a new rating for this app."""

    # if the user isn't signed in, send them to the login screen
    if not request.user.is_authenticated():
        messages.add_message(request, messages.INFO, "You mussed be logged in to rate an App")
        return HttpResponseRedirect('/login')

    app = App.objects.get(pk=pk)
    
    # check to see if the user has already reviewed this App
    try:
        review = Review.objects.get(app__id=app.id, reviewer__id=request.user.id) 
    except:
        review = Review()

    review.app = app
    review.reviewer = request.user
    review.rating = rating
    review.save()

    messages.add_message(request, messages.INFO, "You rated {} {} of 5.".format(app.title, rating))    

    return HttpResponseRedirect("/")


