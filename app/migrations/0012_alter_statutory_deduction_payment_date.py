# Generated by Django 5.1 on 2024-11-30 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_statutory_deduction_deduction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statutory_deduction',
            name='payment_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
