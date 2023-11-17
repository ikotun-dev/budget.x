from django.urls import path, include
from . import views

urlpatterns = [
    path("home/", views.index, name='home'),
    path("signup", views.signup, name='signup'),
    path("dashboard", views.dashboard, name='dashboard'),

]