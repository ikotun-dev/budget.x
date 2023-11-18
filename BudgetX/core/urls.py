from django.urls import path, include
from . import views

urlpatterns = [
    path("home/", views.index, name='home'),
    path("signup", views.signup, name='signup'),
    path("add-expense", views.add_expense, name='add-expense'),
    path("add-budget", views.add_budget, name='add-budget'),
      path("history", views.history, name='history')

]