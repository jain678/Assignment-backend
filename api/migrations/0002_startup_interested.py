# Generated by Django 4.1.5 on 2024-02-03 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="startup",
            name="interested",
            field=models.ManyToManyField(blank=True, to="api.investor"),
        ),
    ]