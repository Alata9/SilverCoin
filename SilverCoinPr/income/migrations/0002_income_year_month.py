# Generated by Django 4.1.5 on 2023-02-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("income", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="income",
            name="year_month",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
