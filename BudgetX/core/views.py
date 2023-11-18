from django.shortcuts import render
from . import models

# Create your views here.
def index(request) : 
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_family = models.Family.objects.filter(username=username)
        if check_family.exists() : 
            context = { 
                "error" : "user does not exist"
            }
            return render (request, context)
        else : 
            print("does not exists")

    return render(request, 'index.html')

def signup(request) : 
    return render(request, 'signup.html')

def add_expense(request) : 
    return render(request, 'add_expense.html')

def add_budget(request) : 
    return render(request, 'add_budget.html')