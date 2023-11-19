from django.db import models

# Create your models here.
class Family(models.Model) : 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    family_no = models.IntegerField()
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'family'

class Expense(models.Model)  : 
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField(default=0)
    category = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    family = models.ForeignKey(Family, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'expense'

class Budget(models.Model)  : 
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    budget_amount = models.IntegerField(null=True)
    
    # Foreign key relationship with Family model
    family = models.ForeignKey(Family, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'budget'

