from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pantry_id>/", views.show, name="show"),
    path("<int:pantry_id>/modify", views.modify, name="modify"), 
]