from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime
from .models import Teacher, Budget
# Create your views here.

def home1(request):
    return render(request, 'home1.html')

def secretary(request):
    teachers_counts = Teacher.objects.all().count()
    return render(request, 'secretary.html',{'teachers_counts':teachers_counts})

def finance(request):
    return render(request, 'finance.html')

def president(request):
    return render(request, 'president.html')



def teachers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        district = request.POST.get('district')
        province = request.POST.get('province')
        pin_code = request.POST.get('pin_code')
        subjects_taught = request.POST.get('subjects_taught')
        schools_taught = request.POST.get('schools_taught')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        profile_picture = request.FILES.get('profile_picture')
        time_of_service = request.POST.get('time_of_service')


        try:
            teacher = Teacher(
                name=name,
                dob=datetime.strptime(dob, '%Y-%m-%d').date(),
                gender=gender,
                district=district,
                province=province,
                pin_code=pin_code,
                subjects_taught=subjects_taught,
                schools_taught=schools_taught,
                email=email,
                phone_number=phone_number,
                address=address,
                profile_picture=profile_picture,
                time_of_service=time_of_service
            )
            teacher.save()
            messages.success(request, "Teacher added successfully!")
            return redirect('teachers')  # Adjust redirect to your desired view
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('teachers')

    # Fetch all teacher records
    teachers = Teacher.objects.all()


    gender_choices = Teacher.gender_choices
    district_choices = Teacher.district_choices
    province_choices = Teacher.province_choices

    return render(request, 'teachers.html', {
        'gender_choices': gender_choices,
        'district_choices': district_choices,
        'province_choices': province_choices,
        'teachers': teachers,
    })


def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)  # Fetch the teacher to edit
    
    if request.method == 'POST':
        # Update teacher details from the form
        teacher.name = request.POST.get('name')
        teacher.dob = request.POST.get('dob')
        teacher.gender = request.POST.get('gender')
        teacher.district = request.POST.get('district')
        teacher.province = request.POST.get('province')
        teacher.pin_code = request.POST.get('pin_code')
        teacher.subjects_taught = request.POST.get('subjects_taught')
        teacher.schools_taught = request.POST.get('schools_taught')
        teacher.email = request.POST.get('email')
        teacher.phone_number = request.POST.get('phone_number')
        teacher.address = request.POST.get('address')
        profile_picture = request.FILES.get('profile_picture')
        teacher.time_of_service = request.POST.get('time_of_service')


        if profile_picture:  # Update profile picture if a new one is uploaded
            teacher.profile_picture = profile_picture
        
        try:
            teacher.save()
            messages.success(request, "Teacher information updated successfully!")
            return redirect('teachers')  # Redirect to the teacher list view
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

    gender_choices = Teacher.gender_choices
    district_choices = Teacher.district_choices
    province_choices = Teacher.province_choices

    return render(request, 'edit_teacher.html', {
        'teacher': teacher,
        'gender_choices': gender_choices,
        'district_choices': district_choices,
        'province_choices': province_choices,
    })


def delete_teacher(request, teacher_id):
    # Get the teacher object by its id (or pin_code, depending on your model setup)
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == 'POST':
        teacher.delete()  # Delete the teacher
        messages.success(request, "Teacher deleted successfully!")
        return redirect('teachers')  # Redirect to the teachers list page

    # If the method is GET, you can render a confirmation page or a simple confirmation message
    return render(request, 'delete_teacher.html', {'teacher': teacher})


def teacher_details(request, teacher_id):
    # Get the teacher object by its id
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    return render(request, 'teacher_details.html', {'teacher': teacher})


def finance_teachers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        district = request.POST.get('district')
        province = request.POST.get('province')
        pin_code = request.POST.get('pin_code')
        subjects_taught = request.POST.get('subjects_taught')
        schools_taught = request.POST.get('schools_taught')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        profile_picture = request.FILES.get('profile_picture')

        try:
            teacher = Teacher(
                name=name,
                dob=datetime.strptime(dob, '%Y-%m-%d').date(),
                gender=gender,
                district=district,
                province=province,
                pin_code=pin_code,
                subjects_taught=subjects_taught,
                schools_taught=schools_taught,
                email=email,
                phone_number=phone_number,
                address=address,
                profile_picture=profile_picture
            )
            teacher.save()
            messages.success(request, "Teacher added successfully!")
            return redirect('finance_teachers')  # Adjust redirect to your desired view
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('finance_teachers')

    # Fetch all teacher records
    teachers = Teacher.objects.all()


    gender_choices = Teacher.gender_choices
    district_choices = Teacher.district_choices
    province_choices = Teacher.province_choices

    return render(request, 'finance_teachers.html', {
        'gender_choices': gender_choices,
        'district_choices': district_choices,
        'province_choices': province_choices,
        'teachers': teachers,
    })


def finance_teachers_details(request, teacher_id):
    # Get the teacher object by its id
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    return render(request, 'finance_teachers_details.html', {'teacher': teacher})

def budget(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        budget_date = request.POST.get('budget_date')
        executive_salary = request.POST.get('executive_salary')
        admin_salary = request.POST.get('admin_salary')
        leave_allowance = request.POST.get('leave_allowance')
        acting_allowance = request.POST.get('acting_allowance')
        on_the_job_training = request.POST.get('on_the_job_training')
        paye_cost = request.POST.get('paye_cost')
        security_cost = request.POST.get('security_cost')
        audit_cost = request.POST.get('audit_cost')
        fuel_cost = request.POST.get('fuel_cost')
        internal_transport = request.POST.get('internal_transport')
        light_bill = request.POST.get('light_bill')
        labor_affiliate = request.POST.get('labor_affiliate')
        water_rate = request.POST.get('water_rate')
        medical_allowance = request.POST.get('medical_allowance')
        financial_assistance = request.POST.get('financial_assistance')
        education_assistance = request.POST.get('education_assistance')
        berievement = request.POST.get('berievement')
        

        try:
            budget = Budget(
                name=name,
                budget_date=datetime.strptime(budget_date, '%Y-%m-%d').date(),
                executive_salary=executive_salary,
                admin_salary=admin_salary,
                leave_allowance=leave_allowance,
                acting_allowance=acting_allowance,
                on_the_job_training=on_the_job_training,
                paye_cost=paye_cost,
                security_cost=security_cost,
                audit_cost=audit_cost,
                fuel_cost=fuel_cost,
                light_bill=light_bill,
                internal_transport=internal_transport,
                water_rate=water_rate,
                labor_affiliate=labor_affiliate,
                medical_allowance=medical_allowance,
                financial_assistance=financial_assistance,
                education_assistance=education_assistance,
                berievement=berievement,
            )
            budget.save()
            messages.success(request, "Budget added successfully!")
            return redirect('budget')  
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('budget')

    budget = Budget.objects.all()
    return render(request, 'budget.html', {
        'budget': budget,
    })


def edit_budget(request, budget_id):
    budget = get_object_or_404(Budget, id=budget_id)
    
    if request.method == 'POST':
        try:
            budget.name = request.POST.get('name')
            budget.budget_date = datetime.strptime(request.POST.get('budget_date'), '%Y-%m-%d').date()
            budget.executive_salary = request.POST.get('executive_salary')
            budget.admin_salary = request.POST.get('admin_salary')
            budget.leave_allowance = request.POST.get('leave_allowance')
            budget.acting_allowance = request.POST.get('acting_allowance')
            budget.on_the_job_training = request.POST.get('on_the_job_training')
            budget.paye_cost = request.POST.get('paye_cost')
            budget.security_cost = request.POST.get('security_cost')
            budget.audit_cost = request.POST.get('audit_cost')
            budget.fuel_cost = request.POST.get('fuel_cost')
            budget.internal_transport = request.POST.get('internal_transport')
            budget.light_bill = request.POST.get('light_bill')
            budget.labor_affiliate = request.POST.get('labor_affiliate')
            budget.water_rate = request.POST.get('water_rate')
            budget.medical_allowance = request.POST.get('medical_allowance')
            budget.financial_assistance = request.POST.get('financial_assistance')
            budget.education_assistance = request.POST.get('education_assistance')
            budget.berievement = request.POST.get('berievement')
            
            budget.save()
            messages.success(request, "Budget updated successfully!")
            return redirect('budget')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    
    return render(request, 'edit_budget.html', {'budget': budget})


def budget_details(request, budget_id):
    # Get the teacher object by its id
    budget = get_object_or_404(Budget, id=budget_id)
    total_budget = budget.get_total_budget()
    
    return render(request, 'budget_details.html', {'budget': budget,'total_budget':total_budget})



def president_budget(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        budget_date = request.POST.get('budget_date')
        executive_salary = request.POST.get('executive_salary')
        admin_salary = request.POST.get('admin_salary')
        leave_allowance = request.POST.get('leave_allowance')
        acting_allowance = request.POST.get('acting_allowance')
        on_the_job_training = request.POST.get('on_the_job_training')
        paye_cost = request.POST.get('paye_cost')
        security_cost = request.POST.get('security_cost')
        audit_cost = request.POST.get('audit_cost')
        fuel_cost = request.POST.get('fuel_cost')
        internal_transport = request.POST.get('internal_transport')
        light_bill = request.POST.get('light_bill')
        labor_affiliate = request.POST.get('labor_affiliate')
        water_rate = request.POST.get('water_rate')
        medical_allowance = request.POST.get('medical_allowance')
        financial_assistance = request.POST.get('financial_assistance')
        education_assistance = request.POST.get('education_assistance')
        berievement = request.POST.get('berievement')
        

        try:
            budget = Budget(
                name=name,
                budget_date=datetime.strptime(budget_date, '%Y-%m-%d').date(),
                executive_salary=executive_salary,
                admin_salary=admin_salary,
                leave_allowance=leave_allowance,
                acting_allowance=acting_allowance,
                on_the_job_training=on_the_job_training,
                paye_cost=paye_cost,
                security_cost=security_cost,
                audit_cost=audit_cost,
                fuel_cost=fuel_cost,
                light_bill=light_bill,
                internal_transport=internal_transport,
                water_rate=water_rate,
                labor_affiliate=labor_affiliate,
                medical_allowance=medical_allowance,
                financial_assistance=financial_assistance,
                education_assistance=education_assistance,
                berievement=berievement,
            )
            budget.save()
            messages.success(request, "Budget added successfully!")
            return redirect('president_budget')  
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('president_budget')

    budget = Budget.objects.all()
    return render(request, 'president_budget.html', {
        'budget': budget,
    })
