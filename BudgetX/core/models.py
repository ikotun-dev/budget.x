from django.db import models

# Create your models here.
class Family(models.Model) : 
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    family_no = models.IntegerField()

class Expense(models.Model)  : 
    id = models.IntegerField(primary_key=True)
    amount = models.IntegerField()
