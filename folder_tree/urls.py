from django.urls import path
from folder_tree import views

urlpatterns = [
    path('', views.index, name = 'homepage'),
]