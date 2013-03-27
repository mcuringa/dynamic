from django.db import models
from django.forms import ModelForm
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User


class App(models.Model):
    """An iPad App that can be rated"""

    title = models.CharField(max_length=500)
    developer = models.CharField(max_length=500, null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    cost = models.DecimalField(max_digits=8,decimal_places=2, null=True, blank=True)
    creator = models.ForeignKey(User,  related_name='app_creators')
    modifier = models.ForeignKey(User,  related_name='app_modifiers')

    def num_ratings(self):
        """The total number of times this App has been rated."""
        
        return len(self.review_set.all())

    def rating(self):
        """The average rating across all reviews."""
        
        ratings = [r.rating for r in self.review_set.all()]
        if len(ratings) == 0:
            return 0
        
        return round(sum(ratings)/len(ratings),1)
        
    def __str__(self):
        return "{} (id:{})".format(self.title, self.id)    
    
    def __unicode__(self):
        return self.title

    class Meta:
            ordering = ('title',)

class AppForm(ModelForm):
    """A ModelForm for editing App Models"""
    class Meta:
        model = App
        exclude = ["creator", "modifier"]


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
        
