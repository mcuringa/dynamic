from django.db import models
from django.forms import ModelForm
from django.template.defaultfilters import slugify

class App(models.Model):
    """An iPad App that can be rated"""

    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, null=True)
    developer = models.CharField(max_length=500, null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    cost = models.DecimalField(max_digits=8,decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    num_ratings = models.IntegerField(null=True)

    def clean(self):
        """Prepare the data to be saved."""

        self.slug = strip_and_test(self.slug)
        if self.slug == None:
            self.slug = slugify(self.title)

        self.url = strip_and_test(self.url)
        if self.url is not None and not self.url.startswith("http"):
            self.url = "http://" + self.url

        

    def __unicode__(self):
        return self.title

    def rate(self, new_rating):
        """Add a new user rating to this app"""
        if(new_rating in range(1,6)):
            self.num_ratings += 1
            self.rating = round((self.rating + new_rating) / self.num_ratings, 1)
        else:
            print("Warn: rating ({}) out of range".format(new_rating))


def strip_and_test(s):
    """Returns None for empty strings, or stripped string"""
    if s == None:
        return None
    
    s = s.strip()
    if len(s) == 0:
        return None
    return s

class AppForm(ModelForm):
    class Meta:
        model = App
        exclude = ["rating","num_ratings", "slug"]
