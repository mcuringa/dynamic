# apps.py
# An application for tracking apps4education


class App(object):
    """An iPad App that can be rated"""
    
    def __init__(self, title, tags="", developer="", url="", cost=-1):
        """Create a new App with title, and tags, developer, url, and cost options"""
        
        # set all of the basic information
        self.title = title
        self.developer = developer
        self.url = url
        self.cost = cost
        self.rating = 0
        self.num_ratings = 0
    
    def rate(self, new_rating):
        """Add a new user rating to this app"""
        if(new_rating in range(1,6)):
            self.num_ratings += 1
            self.rating = round((self.rating + new_rating) / self.num_ratings, 1)
        else:
            print("Warn: rating ({}) out of range".format(new_rating))
        




def main():
    
    angry = App("Angry Birds", cost=0)
    print("Add the valid ratings")
    angry.rate(1)
    angry.rate(5)
    angry.rate(4)

    print("add invalid ratings, make sure they are rejected")
    angry.rate(0)
    angry.rate(6)
    angry.rate(100)
    
    print("-------------")
    print(angry.rating)
    print(angry)


if __name__ == '__main__':
    main()
