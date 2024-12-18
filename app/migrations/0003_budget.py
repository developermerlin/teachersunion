# Generated by Django 5.1 on 2024-11-17 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_teacher_province'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('budget_date', models.DateField()),
                ('executive_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('admi_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('leave_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('acting_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('on_the_job_traninig', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paye_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('security_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('audit_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fuel_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('internal_transport', models.DecimalField(decimal_places=2, max_digits=10)),
                ('light_bill', models.DecimalField(decimal_places=2, max_digits=10)),
                ('water_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('labor_affiliate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('medical_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('financial_assistance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('education_assistance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('berievement', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
