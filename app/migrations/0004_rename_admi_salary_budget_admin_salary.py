# Generated by Django 5.1 on 2024-11-18 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_budget'),
    ]

    operations = [
        migrations.RenameField(
            model_name='budget',
            old_name='admi_salary',
            new_name='admin_salary',
        ),
    ]
