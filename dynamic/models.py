from django.db import models



class App(models.Model):
    """An iPad App that can be rated"""

    title = models.CharField(max_length=500)
    developer = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    cost = models.DecimalField(max_digits=8,decimal_places=2)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    num_ratings = models.IntegerField()


    def rate(self, new_rating):
        """Add a new user rating to this app"""
        if(new_rating in range(1,6)):
            self.num_ratings += 1
            self.rating = round((self.rating + new_rating) / self.num_ratings, 1)
        else:
            print("Warn: rating ({}) out of range".format(new_rating))
