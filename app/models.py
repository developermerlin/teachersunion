from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    district_choices = [
        ('Kailahun', 'Kailahun'),
        ('Kenema', 'Kenema'),
        ('Kono', 'Kono'),
        ('Bombali', 'Bombali'),
        ('Falaba', 'Falaba'),
        ('Koinadugu', 'Koinadugu'),
        ('Tonkolili', 'Tonkolili'),
        ('Kambia', 'Kambia'),
        ('Karene', 'Karene'),
        ('Port Loko', 'Port Loko'),
        ('Bo', 'Bo'),
        ('Bonthe', 'Bonthe'),
        ('Moyamba', 'Moyamba'),
        ('Pujehun', 'Pujehun'),
        ('Western Rural', 'Western Rural'),
        ('Western Urban', 'Western Urban'),
    ]

    province_choices = [
        ('Eastern', 'Eastern'),
        ('Northern', 'Northern'),
        ('Southern', 'Southern'),
        ('Western Rural', 'Western Rural'),
        ('Western Urban', 'Western Urban'),
        
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    district = models.CharField(max_length=100, choices=district_choices)
    province = models.CharField(max_length=100, choices=province_choices)

    
    # Employment details
    pin_code = models.CharField(max_length=20, unique=True)  # Unique ID for the teacher
    subjects_taught = models.TextField(help_text="List of subjects separated by commas")
    schools_taught = models.TextField(help_text="List of subjects separated by commas")
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='teacher_profiles/', blank=True, null=True)
    time_of_service = models.IntegerField()
    def __str__(self):
        return f"{self.name}  - {self.pin_code}"

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"


class Budget(models.Model):
    name = models.CharField(max_length=300)
    budget_date =  models.DateField()
    executive_salary = models.DecimalField(max_digits=10, decimal_places=2)
    admin_salary = models.DecimalField(max_digits=10, decimal_places=2)
    leave_allowance =  models.DecimalField(max_digits=10, decimal_places=2)
    acting_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    on_the_job_training = models.DecimalField(max_digits=10, decimal_places=2)
    paye_cost = models.DecimalField(max_digits=10, decimal_places=2)
    security_cost = models.DecimalField(max_digits=10, decimal_places=2)
    audit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_cost =  models.DecimalField(max_digits=10, decimal_places=2)
    internal_transport =  models.DecimalField(max_digits=10, decimal_places=2)
    light_bill =  models.DecimalField(max_digits=10, decimal_places=2)
    water_rate =  models.DecimalField(max_digits=10, decimal_places=2)
    labor_affiliate = models.DecimalField(max_digits=10, decimal_places=2)
    medical_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    financial_assistance =  models.DecimalField(max_digits=10, decimal_places=2)
    education_assistance = models.DecimalField(max_digits=10, decimal_places=2)
    berievement =  models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"{self.name}  - {self.budget_date}"
    def get_total_budget(self):
        return (
            self.executive_salary +
            self.admin_salary +
            self.leave_allowance +
            self.acting_allowance +
            self.on_the_job_training +
            self.paye_cost +
            self.security_cost +
            self.audit_cost +
            self.fuel_cost +
            self.internal_transport +
            self.light_bill +
            self.water_rate +
            self.labor_affiliate +
            self.medical_allowance +
            self.financial_assistance +
            self.education_assistance +
            self.berievement
        )



