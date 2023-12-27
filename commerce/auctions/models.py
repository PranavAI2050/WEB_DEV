from django.contrib.auth.models import AbstractUser
from django.db import models


 

class Listing(models.Model):
    title = models.CharField(max_length = 64)
    description  = models.TextField()
    image = models.URLField(max_length=200, null= True, blank = True)
    active = models.BooleanField()
    categorie = models.CharField(max_length = 64)
#created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.categorie}"

class User(AbstractUser,models.Model):
    Watchlist = models.ManyToManyField(Listing, related_name = "items", blank = True)

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete  = models.CASCADE, related_name = "comment")
    
    def __str__(self):
        return f"comment by {self.user.username} on {self.listing.title} : {self.comment[:50]}"
    
class Bid(models.Model):
    bid  = models.IntegerField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    listing = models.ForeignKey(Listing,on_delete = models.CASCADE, related_name = "bid")

    def __str__(self):
        return f"bid by {self.user.username} on {self.listing.title} : {self.bid}"
