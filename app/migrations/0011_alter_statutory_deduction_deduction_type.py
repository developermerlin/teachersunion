# Generated by Django 5.1 on 2024-11-30 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_statutory_deduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statutory_deduction',
            name='deduction_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
