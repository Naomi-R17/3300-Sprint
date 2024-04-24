# Generated by Django 4.2 on 2024-04-24 04:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("care_app", "0008_delete_registereduser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medication",
            name="endDate",
            field=models.DateField(blank=True, verbose_name="Ending Date"),
        ),
        migrations.AlterField(
            model_name="medication",
            name="startDate",
            field=models.DateField(blank=True, verbose_name="Starting Date"),
        ),
    ]
