# Auction Site  

## Overview

Welcome to the Auction Site project! This web application is built using Django and designed to facilitate online auctions. Users can create, browse, and bid on auction listings, as well as manage their watchlist. The application also includes features such as commenting and categorization.

## Features

## ScreenShort
https://github.com/PranavAI2050/WEB_DEV/assets/123180829/4d05b2d8-0a35-4e5d-a33b-6675b295a799



### Models

1. **User Model**
   - Default Django User model extended.

2. **Auction Listings Model**
   - Fields: title, description, starting bid, current price, image URL (optional), category, and status (active/closed).

3. **Bids Model**
   - Fields: bidder, listing, bid amount.

4. **Comments Model**
   - Fields: commenter, listing, comment text.

### Create Listing

- Users can create a new listing by providing a title, description, starting bid, optional image URL, and category.

### Active Listings Page

- The default route displays all currently active auction listings.
- For each listing, it shows title, description, current price, and a photo (if available).

### Listing Page

- Clicking on a listing provides detailed information, including the current price.
- Signed-in users can add the item to their watchlist or bid on the item.
- Listing creator can close the auction, declaring the highest bidder as the winner.

### Watchlist

- Users can view all the listings they have added to their watchlist.
- Clicking on a listing in the watchlist redirects to that listing's page.

### Categories

- Users can view a list of all listing categories.
- Clicking on a category displays all active listings in that category.

### Django Admin Interface

- Administrators can manage listings, comments, and bids through the Django admin interface.
- They can view, add, edit, and delete any entries.

## How to Run the Application

1. Clone the repository:
   
   ```bash
   git clone https://github.com/PranavAI2050/WEB_DEV.git
   cd WEB_DEV
   
2. Create a virtual environment activate it :
   ```bash
   python -m venv my_env
   my_env\Scripts\activate
   
3. Install necessary packages :
   ```bash
   pip install django
   
4. go to commerce directory and run the website :
   ```bash
   python manage.py runserver
