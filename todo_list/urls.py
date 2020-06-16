from django.urls import *
from . import views

app_name = 'todo_list'

urlpatterns = [path("", views.index, name="index"),
               path("delete/<str:number>/", views.delete, name="delete"),
               path("update/<str:update>/", views.update, name="update")
               ]

