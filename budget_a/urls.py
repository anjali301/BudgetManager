from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('login/', views.Login, name="login"),
    path('thanks/', views.Thanks, name="thanks"),
    path('register/', views.Register, name="register"),
    path('contact/', views.Contact, name="contact"),
    path('manage-budget/', views.ManageBudget, name="managebudget"),
    path('statistics/', views.Statistics, name="statistics"),
    path('  expstats/', views.ExpStats, name="expstats"),
    path('incstats/', views.IncStats, name="incstats"),
    path('savstats/', views.SavStats, name="savstats"),
    path('logout/', views.Logout, name="logout"),
    path('income/', views.Income, name="income"),
    path('expenses/', views.Expenses, name="expenses"),
    path('savings/', views.Savings, name="savings"),
    path('savings_edit/', views.SavingsEdit, name="savings_edit"),
    path('preferences/', views.Preferences, name="preferences"),
    path('messages/', views.Messages, name="messages"),
    path('addincome/', views.AddIncome, name="addincome"),
    path('addexpense/', views.AddExpense, name="addexpense"),
    path('addsavings/', views.AddSavings, name="addsavings"),
]