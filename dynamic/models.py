from django.db import models
from django import forms
from django.forms import ModelForm
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User


class ContactForm(forms.forms):
    """A contact message, which can be sent via email"""

    #NOTE: this is a form without a model
    # our fields are from the "forms" package, not "models"
    # the difference is that we will not save this to the DB
    subject = forms.CharField(max_length=500)
    from_name = forms.CharField(max_length=500)
    from_email = forms.EmailField(max_length=254)
    message = forms.TextField()




class App(models.Model):
    """An iPad App that can be rated"""

    title = models.CharField(max_length=500)
    developer = models.CharField(max_length=500, null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    cost = models.DecimalField(max_digits=8,decimal_places=2, null=True, blank=True)
    #~ rating = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    #~ num_ratings = models.IntegerField(null=True)
    creator = models.ForeignKey(User,  related_name='app_creators')
    modifier = models.ForeignKey(User,  related_name='app_modifiers')

    def __str__(self):
        return "{} (id:{})".format(self.title, self.id)    
    
    def __unicode__(self):
        return self.title

    def is_free(self):
        """The app is free if the cost is zero"""
        return cost == 0


    def num_ratings(self):
        return len(self.review_set.all())

    def rating(self):
        ratings = [r.rating for r in self.review_set.all()]
        if len(ratings) == 0:
            return 0
        
        return round(sum(ratings)/len(ratings),1)
        
    class Meta:
            ordering = ('title',)

class AppForm(ModelForm):
    """A ModelForm for editing App Models"""
    class Meta:
        model = App
        exclude = ["rating","num_ratings", "creator", "modifier"]


class Review(models.Model):
    """A review and a rating for an App"""

    rating_choices = [(5,5),(4,4),(3,3),(2,2),(1,1)]

    review = models.TextField()
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, choices=rating_choices)
    reviewer = models.ForeignKey(User, null=False)
    app = models.ForeignKey(App, null=False)

    def __str__(self):
        return "(user:{}), (app:{}), (rating:{}), '{}(id:{})'".format(self.reviewer.username, self.app.id, self.rating, self.review, self.id)    



class ReviewForm(ModelForm):
    """A ModelForm for editing App Models"""
    class Meta:
        model = Review
        exclude = ["app", "reviewer"]
        
