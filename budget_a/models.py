from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    income = models.IntegerField(blank=True, default=0)
    expenditure = models.IntegerField(blank=True, default=0)
    savings = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.username


class Expense(models.Model):  
    req_user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    amount = models.IntegerField()
    desc = models.TextField()
    date_of_exp = models.DateField()


class IncomeModel(models.Model):
    req_user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    amount = models.IntegerField()
    desc = models.TextField()
    date_of_inc = models.DateField()


class Saving(models.Model):
    req_user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    amount = models.IntegerField()
    desc = models.TextField()
    date_of_saving = models.DateField()
