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

    def save(self,*args, **kwargs):
        """Set the slug, from the title, when it's saved the first time"""
        if self.slug == None or len(self.slug) == 0:
            self.slug = slugify(self.title)
        super(App, self).save()


    def __unicode__(self):
        return self.title

    def rate(self, new_rating):
        """Add a new user rating to this app"""
        if(new_rating in range(1,6)):
            self.num_ratings += 1
            self.rating = round((self.rating + new_rating) / self.num_ratings, 1)
        else:
            print("Warn: rating ({}) out of range".format(new_rating))


class AppForm(ModelForm):
    class Meta:
        model = App
        exclude = ["rating","num_ratings", "slug"]
