from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(request) : 
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_family = models.Family.objects.filter(username=username)
        if check_family.exists() : 
           request.session['username'] = username
           print("user exists")
           return redirect('add-expense')
        else : 
            context = { 
                "error" : "user does not exist"
            }
            return render (request, 'index.html', context)
            print("does not exists")

    return render(request, 'index.html')

def signup(request) : 
    if request.method == "POST" :
        family_name = request.POST.get('family_name')
        no_of_family = request.POST.get('no_of_family')   
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        check_family = models.Family.objects.filter(username=username)
        if check_family.exists() : 
            context = { 
                "error" : "family username already exist"
            }
            return render (request, 'signup.html', context)

        check_family_email = models.Family.objects.filter(email=email)
        if check_family.exists() : 
            context = { 
                "error" : "family email already exist"
            }
            return render (request, 'signup.html', context)
        else : 
            context = { 
                "sucess" : "successfully created, please Login"
            }
           
            new_family = models.Family(name=family_name, family_no=no_of_family, username=username, password=password, email=email)
            new_family.save()
            print("family created succesffully")
            return render (request, 'signup.html', context)


    return render(request, 'signup.html')

def add_expense(request) : 
    username = request.session.get('username')
    print("im now in expense page")
    print("logged in user is : " + " " + username)
    return render(request, 'add_expense.html')

def add_budget(request) : 

    return render(request, 'add_budget.html')