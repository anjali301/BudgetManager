from django.contrib import admin
from .models import UserProfile, Expense, IncomeModel, Saving

admin.site.register([UserProfile, Expense, IncomeModel, Saving])