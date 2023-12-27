from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name = "create"),
    path("listing/<int:id>", views.listing, name = "listing"),
    path("add/<int:id>", views.add, name = "add"),
    path("bid/<int:id>", views.bid, name = "bid"),
    path("close/<int:id>", views.close, name = "close"),
    path("comment/<int:id>", views.comment, name = "comment"),
    path("watch", views.watch, name = "watch"),
    path("cat/<str:cat>", views.getcat, name = "cat")
]
