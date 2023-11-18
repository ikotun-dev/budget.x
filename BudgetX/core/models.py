from django.db import models

# Create your models here.
class Family(models.Model) : 
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    family_no = models.IntegerField()

    class Meta:
        db_table = 'family'

class Expense(models.Model)  : 
    id = models.IntegerField(primary_key=True)
    amount = models.IntegerField(default=0)
    category = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    family_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'expense'

