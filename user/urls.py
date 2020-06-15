from . import views
from django.urls import *

app_name = "user"
urlpatterns = [path('', views.login, name="login"),
               path('signup/', views.signup, name="signup")]
