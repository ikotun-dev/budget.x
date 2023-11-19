from django.shortcuts import render, redirect
from . import models

def home_page(request) : 
    return render(request, 'home.html')
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
                "success" : "successfully created, please Login"
            }
           
            new_family = models.Family(name=family_name, family_no=no_of_family, username=username, password=password, email=email)
            new_family.save()
            print("family created succesffully")
            return render (request, 'signup.html', context)


    return render(request, 'signup.html')

def add_expense(request) : 
    username = request.session.get('username')
    user = models.Family.objects.get(username=username)
    print("im now in expense page")
    print("logged in user is : " + " " + username)
    if request.method == "POST" : 
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        description = request.POST.get('description')
        new_expense = models.Expense(amount=amount, category=category, description=description, family_id=user.id)
        new_expense.save()
        context = { 
                "success" : "Expense successfully added"
            }
        
        print("expense saved successfully")
        print(amount + " " + category + " " + description)
        return render (request, 'add_expense.html', context)


    return render(request, 'add_expense.html')

def add_budget(request) : 
    username = request.session.get('username')
    user = models.Family.objects.get(username=username)
    print("im now in budget page")
    print("logged in user is : " + " " + username)
    if request.method == "POST" : 
        amount = request.POST.get('limit')
        category = request.POST.get('category')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        new_budget = models.Budget(budget_amount=amount, category=category, start_date=start_date, end_date=end_date, family=user)
        new_budget.save()
        context = { 
                "success" : "Expense successfully added"
            }
        return render(request, 'add_budget.html', context)

    return render(request, 'add_budget.html')

def history(request) : 
    
    username = request.session.get('username')
    user = models.Family.objects.get(username=username)
    expenses = models.Expense.objects.filter(family_id=user.id)
    budgets = models.Budget.objects.filter(family_id=user.id)

    #expense value
    expense_value = 0 
    for expense in expenses : 
        expense_value = expense_value + expense.amount
    print(expense_value)

    #budget_value 
    budget_value = 0 
    for budget in budgets : 
        budget_value = budget_value + budget.budget_amount 
    print(budget_value)

    #budget track
    budget_track = budget_value - expense_value


   
    context = { 
        "results" : expenses,
        "budgets" : budgets,
        "budget_track" : budget_track
    }
    return render(request, 'history.html', context)