from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages

from .models import User, Listing, Bid,Comment


def index(request):
    listings = Listing.objects.all()
    categories = listings.values('categorie').distinct()  
    return render(request, "auctions/index.html",{
        "listings" :listings,
         "watching" : False,
         "categories" :categories
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
def create(request):
    listings = Listing.objects.all()
    categories = listings.values('categorie').distinct() 
    if request.method == "POST":
        title= request.POST["title"]
        description=request.POST["description"]
        image = request.POST["image url"]
        categorie = request.POST["categorie"]
        bid = request.POST["starting bid"]
        if not title or not description or not categorie or not bid:
            messages.error(request, 'Please fill out the form completely')
            return redirect('create')
        else:
            listing = Listing(
            title=title,
            description=description,
            image=image,
            categorie=categorie,
            active = True
        )
            listing.save()
            bid = Bid(
                bid = bid,
                user =  request.user,
                listing = listing
            )
            bid.save()
        messages.success(request,'Listing created successfully')
        return render(request, "auctions/index.html",{
            "listings" :listings,
            "watching" : False,
            "categories" :categories,
            "message_listing" : "Listing Created Sucessfully"
              })
    
    else:
        if request.user.is_authenticated:
            return render(request, "auctions/create.html")
        else:
            return render(request, "auctions/login.html")


 
def listing(request, id):
    user = request.user
    listings = Listing.objects.all()
    categories = listings.values('categorie').distinct() 
    if user.is_authenticated:
        listing = Listing.objects.get(id = id)

        exist = user.Watchlist.filter(id=id).exists()
        bid = Bid.objects.filter(listing=listing).first()
        same_user = user == bid.user
        comments = Comment.objects.filter(listing =listing)
        last_bid = Bid.objects.filter(listing=listing).last()
        last_bidder = user == last_bid.user
        return render(request,"auctions/listing.html",{
            "listing":listing,
           "exist":exist,
           "same_user":same_user,
           "comments":comments,
           "last_bid":last_bid.listing.title,
           "last_bidder":last_bidder,
           "amount":last_bid.bid
        })
    else:
        return render(request, "auctions/index.html",{
        "listings" :listings,
         "watching" : False,
         "categories" :categories,
         "log_message":"Please Login To make Bid"
    })
 
def add(request,id):
    listing = Listing.objects.get(id = id)
    user = request.user
    exist = user.Watchlist.filter(id=id).exists()
    bid = Bid.objects.filter(listing=listing).first()
    same_user = user == bid.user
    comments = Comment.objects.filter(listing =listing)
    if not user.Watchlist.filter(id = id).exists():
        user.Watchlist.add(listing)
        return render(request,"auctions/listing.html",{
            "listing":listing,
           "exist":True,
           "same_user":same_user,
           "comments":comments,
           "message_add":True,
           "add":True
        })
    else:
        user.Watchlist.remove(listing)
        return render(request,"auctions/listing.html",{
            "listing":listing,
            "exist":False,
            "same_user":same_user,
            "comments":comments,
            "message_add":False,
            "add":True
        })
def bid(request,id):
    listing = Listing.objects.get(id = id)
    user = request.user
    bid = Bid.objects.filter(listing=listing).first()
    same_user = user == bid.user
    exist = user.Watchlist.filter(id=id).exists()
    comments = Comment.objects.filter(listing =listing)
    if request.method == "POST":
        amount = int(request.POST["bid"])
        if Bid.objects.filter(user = user, listing = listing).exists():
            bid = Bid.objects.filter(listing = listing).last()
            if amount > bid.bid:
                bid.bid = amount
                bid.save()
                return render(request,"auctions/listing.html",{
                    "listing":listing,
                    "exist":exist,
                    "same_user":same_user,
                    "comments":comments,
                    "bid_flag":True,
                    "bidding" :True
                    
                    })
            else:
                return render(request,"auctions/listing.html",{
                    "listing":listing,
                    "exist":exist,
                    "same_user":same_user,
                    "comments":comments,
                     "bid_flag":False,
                     "bidding" :True
                    })
        else :
            bid = Bid(bid = amount,user = user, listing = listing)
            bid.save()
            return render(request,"auctions/listing.html",{
                "listing":listing,
                "exist":exist,
                "same_user":same_user,
                "comments":comments,
                "bid_flag":True,
                "bidding" :True
        })
    else:
        return render(request,"auctions/listing.html",{
            "listing":listing,
            "exist":exist,
            "same_user":same_user,
            "comments":comments,
            "bidding" :False
        })
    
def close(request,id):
    listings = Listing.objects.all()
    listing = Listing.objects.get(id= id)
    bid = Bid.objects.filter(listing=listing).first()
    user = request.user
    exist = user.Watchlist.filter(id=id).exists()
    same_user = user == bid.user
    comments = Comment.objects.filter(listing =listing)
    if request.method == "POST":
        listing.active = False
        listing.save()
        return render(request, "auctions/index.html",{
            "listings" :listings,
            "watching" : False,
            "message_close":"Your Listing Closed Sucessfully"
            })
    else:
        return render(request,"auctions/listing.html",{
            "listing":listing,
            "exist":exist,
            "same_user":same_user,
            "comments":comments
        })

def comment(request,id):
    listing = Listing.objects.get(id= id)
    bid = Bid.objects.filter(listing=listing).first()
    user = request.user
    exist = user.Watchlist.filter(id=id).exists()
    same_user = user == bid.user
    comments = Comment.objects.filter(listing =listing)
    if request.method == "POST":
        text = request.POST["comment"]
        comment = Comment(comment = text,user = user, listing = listing)
        comment.save()
        return render(request,"auctions/listing.html",{
            "listing":listing,
            "exist":exist,
            "same_user":same_user,
            "comments":comments
        })
    else:
        return render(request,"auctions/listing.html",{
            "listing":listing,
            "exist":exist,
            "same_user":same_user,
            "comments":comments
        })
    
def watch(request):
    listings = Listing.objects.all()
    user = request.user
    watch_list = user.Watchlist.all()
    categories = listings.values('categorie').distinct() 
    return render(request, "auctions/index.html",{
        "listings" :watch_list,
        "watching" : True,
        "categories" :categories
    })


def getcat(request, cat):
    listings_cat = Listing.objects.filter(categorie = cat)
    listings = Listing.objects.all()
    categories = listings.values('categorie').distinct() 
    return render(request, "auctions/index.html",{
        "listings" :listings_cat,
         "watching" : False,
         "categories" :categories,
         "message_cat":f"Here Are some Results of {cat} Items"
    })