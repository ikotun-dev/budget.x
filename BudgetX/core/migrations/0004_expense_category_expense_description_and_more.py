# Generated by Django 4.2.7 on 2023-11-18 21:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_alter_family_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="category",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="expense",
            name="description",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="expense",
            name="family_id",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="expense",
            name="amount",
            field=models.IntegerField(default=0),
        ),
    ]
