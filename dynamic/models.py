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
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    num_ratings = models.IntegerField(null=True)
    created_by = models.ForeignKey(User,  related_name='app_creators')
    modified_by = models.ForeignKey(User,  related_name='app_modifiers')
    
    def __unicode__(self):
        return self.title

    def is_free(self):
        """The app is free if the cost is zero"""
        return cost == 0

    def rate(self, new_rating):
        """Add a new user rating to this app"""
        if(new_rating in range(1,6)):
            if self.num_ratings == None:
                self.num_ratings = 0
                self.rating = 0

            # sum of all ratings so far
            
            ratings = self.rating * self.num_ratings
            self.num_ratings += 1
            ratings += new_rating
            self.rating = round( ratings / self.num_ratings, 1)
        else:
            print("Warn: rating ({}) out of range".format(new_rating))

class AppForm(ModelForm):
    """A ModelForm for editing App Models"""
    class Meta:
        model = App
        exclude = ["rating","num_ratings", "created_by", "modified_by"]


class Review(models.Model):
    """A review and a rating for an App"""
    reviewer = models.CharField(max_length=500)
    review = models.TextField()
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    reviewer = models.ForeignKey(User, null=False)


