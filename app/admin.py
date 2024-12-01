from django.contrib import admin
from .models import Teacher,Budget,President_Message,Salary_Allowance,Statutory_Deduction,Running_Cost

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Budget)
admin.site.register(President_Message)
admin.site.register(Salary_Allowance)
admin.site.register(Statutory_Deduction)
admin.site.register(Running_Cost)
