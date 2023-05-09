from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view/", views.show, name="show"),
    path("add/", views.add_ingredient, name="add"), 
    path("modify/", views.modify, name="modify"),
    path("logout/", views.logout_view, name="logout"),  
]