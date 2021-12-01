from django.shortcuts import render, redirect
from .models import UserProfile, Expense, IncomeModel, Saving
from django.contrib import messages
from django.contrib.auth.models import auth
from django.http import HttpResponse
import json
from django.db.models import Sum

from django.views.generic import View 
from rest_framework.views import APIView 
from rest_framework.response import Response

def Thanks(request):
    return render(request, 'thanks.html')


def Savings(request):
    return render(request, 'savings/index.html')


def Home(request):
    return render(request, 'home.html')


def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserProfile.objects.get(username=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/manage-budget')
        except:
            messages.info(request, 'Invalid Credentials!')
            return redirect('/login')
    else:
        return render(request, 'login.html')


def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        if(password == repassword):
            if(UserProfile.objects.filter(username=email).exists()):
                messages.info(request, 'A user with this email address already exists!')
                return redirect('/register')
            else:
                user = UserProfile.objects.create(first_name=fname, last_name=lname, username=email, password=password)
                user.save()
                return redirect('/login')
        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('/register')
    else:
        return render(request, 'register.html')


def Logout(request):
    auth.logout(request)
    return redirect('/login')


def Contact(request):
    return render(request, 'contact.html')


def SavingsEdit(request):
    return render(request, 'savings/edit_savings.html')


def ManageBudget(request):
    return render(request, 'managebudget.html')


def Income(request):
    return render(request, 'income/index.html')


def Expenses(request):
    return render(request, 'expense/index.html')


def AddIncome(request):
    if request.method == "POST":
        user = request.user
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        income_date = request.POST.get('income_date')
        inc = IncomeModel.objects.create(req_user=user, amount=amount, desc=description, date_of_inc=income_date)
        inc.save()
        return redirect('/manage-budget')
    else:
        return render(request, 'income/add_income.html')


def AddExpense(request):
    if request.method == "POST":
        user = request.user
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        expense_date = request.POST.get('expense_date')
        exp = Expense.objects.create(req_user=user, amount=amount, desc=description, date_of_exp=expense_date)
        exp.save()
        return redirect('/manage-budget')
    else:    
        return render(request, 'expense/add_expense.html')


def AddSavings(request):
    if request.method == "POST":
        user = request.user
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        saving_date = request.POST.get('saving_date')
        user_saving = Saving.objects.create(req_user=user, amount=amount, desc=description, date_of_saving=saving_date)
        user_saving.save()
        return redirect('/manage-budget')
    else:
        return render(request, 'savings/add_savings.html')


def Statistics(request):        # updated
    user = request.user
    total_exp = Expense.objects.filter(req_user=user)
    total_inc = IncomeModel.objects.filter(req_user=user)
    total_savings = Saving.objects.filter(req_user=user)
    exp = 0
    inc = 0
    saving = 0
    for query in total_exp:
        exp += int(query.amount)
    for query in total_inc:
        inc += int(query.amount)
    for query in total_savings:
        saving += int(query.amount)
    context = {
        'x':exp,
        'y':inc,
        'z':saving
    }
    return render(request, 'statistics.html', context)


def ExpStats(request):
    user = request.user
    exp = Expense.objects.filter(req_user=user).order_by('-id')
    context = {
        'exp' : exp
    }
    return render(request, 'expense/stats.html', context)


def IncStats(request):
    user = request.user
    inc = IncomeModel.objects.filter(req_user=user).order_by('-id')
    context = {
        'inc' : inc
    }
    return render(request, 'income/stats.html', context)


def SavStats(request):
    user = request.user
    sav = Saving.objects.filter(req_user=user).order_by('-id')
    context = {
        'sav' : sav
    }
    return render(request, 'savings/stats.html', context)


def Preferences(request):
    return render(request, 'preferences.html')


def Messages(request):
    return render(request, 'messages.html')


class HomeView (View): 
	def get(self, request, *args, **kwargs): 
		return render(request, 'chartjs/index.html') 