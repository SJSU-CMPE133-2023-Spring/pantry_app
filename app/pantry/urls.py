from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view/", views.show, name="show"),
    path("add/", views.add_ingredient, name="add"), 
    path("modify/", views.modify, name="modify"),
    path("logout/", views.logout_view, name="logout"), 
    
    path('my-pantry/', views.myPantry, name="my-pantry"),
    path('add-item/', views.addItem, name="add-item"),
    path('delete-item/<str:pk>/', views.deleteItem, name="delete-item"),
    path('edit-item/<str:pk>/', views.editItem, name="edit-item"), 
]