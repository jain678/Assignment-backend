# Generated by Django 4.1.5 on 2024-02-03 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_startup_interested"),
    ]

    operations = [
        migrations.AddField(
            model_name="startup",
            name="csv_file",
            field=models.FileField(blank=True, upload_to="media"),
        ),
    ]
