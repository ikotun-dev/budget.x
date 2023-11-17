from django.shortcuts import render

# Create your views here.
def index(request) : 
    return render(request, 'index.html')

def signup(request) : 
    return render(request, 'signup.html')

def add_expense(request) : 
    return render(request, 'add_expense.html')

def add_budget(request) : 
    return render(request, 'add_budget.html')