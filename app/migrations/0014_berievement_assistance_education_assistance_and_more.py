# Generated by Django 5.1 on 2024-12-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_running_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Berievement_Assistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('welfare_type', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Education_Assistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('welfare_type', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Financial_Assistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('welfare_type', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Medical_Assistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('welfare_type', models.CharField(blank=True, max_length=200, null=True)),
                ('payment_cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]