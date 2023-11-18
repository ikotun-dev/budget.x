# Generated by Django 4.2.7 on 2023-11-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Expense",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("amount", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Family",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("username", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
                ("family_no", models.IntegerField()),
            ],
        ),
    ]