from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime
from .models import Teacher, Budget, President_Message,Finance_Message,Salary_Allowance,Statutory_Deduction,Running_Cost,Medical_Assistance,Financial_Assistance,Berievement_Assistance,Education_Assistance
# Create your views here.

def home1(request):
    return render(request, 'home1.html')

def secretary(request):
    teachers_counts = Teacher.objects.all().count()
    budget_counts = Teacher.objects.all().count()
    message = President_Message.objects.all().count()
    return render(request, 'secretary.html',{'teachers_counts':teachers_counts,'budget_counts':budget_counts,'message':message})

def finance(request):
    teachers = Teacher.objects.all().count()
    budget = Budget.objects.all().count()
    context = {
        'teachers':teachers,
        'budget':budget,
    }

    return render(request, 'finance.html',context)


def president(request):
    teachers = Teacher.objects.all().count()
    budget = Budget.objects.all().count()
    message = Finance_Message.objects.all().count()
    salary_allowance = Salary_Allowance.objects.all().count()
    statutory_deduction = Statutory_Deduction.objects.all().count()
    running_cost = Running_Cost.objects.all().count()
    context = {
        'teachers':teachers,
        'budget':budget,
        'message':message,
        'salary_allowance':salary_allowance,
        'statutory_deduction':statutory_deduction,
        'running_cost':running_cost
    }
    return render(request, 'president.html',context)



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


def president_budget_details(request, budget_id):
    # Get the teacher object by its id
    budget = get_object_or_404(Budget, id=budget_id)
    total_budget = budget.get_total_budget()
    
    return render(request, 'president_budget_details.html', {'budget': budget,'total_budget':total_budget})


def president_teachers(request):
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
            return redirect('president_teachers')  # Adjust redirect to your desired view
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('president_teachers')

    # Fetch all teacher records
    teachers = Teacher.objects.all()


    gender_choices = Teacher.gender_choices
    district_choices = Teacher.district_choices
    province_choices = Teacher.province_choices

    return render(request, 'president_teachers.html', {
        'gender_choices': gender_choices,
        'district_choices': district_choices,
        'province_choices': province_choices,
        'teachers': teachers,
    })


def president_teachers_details(request, teacher_id):
    # Get the teacher object by its id
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    return render(request, 'president_teachers_details.html', {'teacher': teacher})

def president_messages(request):
    if request.method == 'POST':
        message_date = request.POST.get('message_date')
        message_subject = request.POST.get('message_subject')
        message_body = request.POST.get('message_body')
       


        try:
            message = President_Message(
                message_subject=message_subject,
                message_date=datetime.strptime(message_date, '%Y-%m-%d').date(),
                message_body=message_body,
               
            )
            message.save()
            messages.success(request, "Message sent successfully!")
            return redirect('president_messages')  # Adjust redirect to your desired view
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('president_messages')

    # Fetch all teacher records
    messaging = President_Message.objects.all()


    return render(request, 'president_messages.html', {
  
        'messaging': messaging,
    })

def edit_president_messages(request, president_id):
    message = get_object_or_404(President_Message, id=president_id)  
    
    if request.method == 'POST':
        message.message_date = request.POST.get('message_date')
        message.message_subject = request.POST.get('message_subject')
        message.message_body = request.POST.get('message_body')
        
        try:
            message.save()
            messages.success(request, "Message  updated successfully!")
            return redirect('president_messages') 
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")


    return render(request, 'edit_president_messages.html', {
        'message': message,
        
    })

def delete_president_message(request, president_id):
    # Get the teacher object by its id (or pin_code, depending on your model setup)
    teacher = get_object_or_404(President_Message, id=president_id)

    if request.method == 'POST':
        teacher.delete()  # Delete the teacher
        messages.success(request, "Message deleted successfully!")
        return redirect('president_messages')  # Redirect to the teachers list page

    # If the method is GET, you can render a confirmation page or a simple confirmation message
    return render(request, 'delete_president_messages.html', {'teacher': teacher})

def president_message_details(request, teacher_id):
    # Get the teacher object by its id
    president = get_object_or_404(President_Message, id=teacher_id)
    
    return render(request, 'president_message_details.html', {'president': president})



def finance_messages(request):
    if request.method == 'POST':
        message_date = request.POST.get('message_date')
        message_subject = request.POST.get('message_subject')
        message_body = request.POST.get('message_body')
        try:
            message = President_Message(
                message_subject=message_subject,
                message_date=datetime.strptime(message_date, '%Y-%m-%d').date(),
                message_body=message_body,
               
            )
            message.save()
            messages.success(request, "Message sent successfully!")
            return redirect('finance_messages')  # Adjust redirect to your desired view
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('finance_messages')

    # Fetch all teacher records
    messaging = President_Message.objects.all()


    return render(request, 'finance_messages.html', {
  
        'messaging': messaging,
    })


def view_president_message_details(request, teacher_id):
    # Get the teacher object by its id
    president = get_object_or_404(President_Message, id=teacher_id)
    
    return render(request, 'view_president_message_details.html', {'president': president})



def message_to_president(request):
    if request.method == 'POST':
        message_date = request.POST.get('message_date')
        message_subject = request.POST.get('message_subject')
        message_body = request.POST.get('message_body')
        try:
            message = Finance_Message(
                message_subject=message_subject,
                message_date=datetime.strptime(message_date, '%Y-%m-%d').date(),
                message_body=message_body,
               
            )
            message.save()
            messages.success(request, "Message sent successfully!")
            return redirect('message_to_president')  # Adjust redirect to your desired view
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('message_to_president')

    # Fetch all teacher records
    messaging = Finance_Message.objects.all()


    return render(request, 'message_to_president.html', {
  
        'messaging': messaging,
    })

def edit_message_to_president(request, president_id):
    message = get_object_or_404(Finance_Message, id=president_id)  
    
    if request.method == 'POST':
        message.message_date = request.POST.get('message_date')
        message.message_subject = request.POST.get('message_subject')
        message.message_body = request.POST.get('message_body')
        
        try:
            message.save()
            messages.success(request, "Message  updated successfully!")
            return redirect('message_to_president') 
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")


    return render(request, 'edit_message_to_president.html', {
        'message': message,
        
    })

def delete_message_to_president(request, president_id):
    # Get the teacher object by its id (or pin_code, depending on your model setup)
    teacher = get_object_or_404(Finance_Message, id=president_id)

    if request.method == 'POST':
        teacher.delete()  # Delete the teacher
        messages.success(request, "Message deleted successfully!")
        return redirect('message_to_president')  # Redirect to the teachers list page

    # If the method is GET, you can render a confirmation page or a simple confirmation message
    return render(request, 'delete_message_to_president.html', {'teacher': teacher})


def message_from_finance(request):
    if request.method == 'POST':
        message_date = request.POST.get('message_date')
        message_subject = request.POST.get('message_subject')
        message_body = request.POST.get('message_body')
        try:
            message = Finance_Message(
                message_subject=message_subject,
                message_date=datetime.strptime(message_date, '%Y-%m-%d').date(),
                message_body=message_body,
               
            )
            message.save()
            messages.success(request, "Message sent successfully!")
            return redirect('message_from_finance')  # Adjust redirect to your desired view
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('message_from_finance')

    # Fetch all teacher records
    messaging = Finance_Message.objects.all()


    return render(request, 'message_from_finance.html', {
  
        'messaging': messaging,
    })



def view_message_from_finance(request, teacher_id):
    # Get the teacher object by its id
    president = get_object_or_404(Finance_Message, id=teacher_id)
    
    return render(request, 'view_message_from_finance.html', {'president': president})


def admin_expenditure(request):
    return render(request, 'admin_expenditure.html')

def salary_allowance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        expenditure_type = request.POST.get('expenditure_type')
        staff_position = request.POST.get('staff_position')
        payment_cost = request.POST.get('payment_cost')

        try:
            Salary_Allowance.objects.create(
                name=name,
                payment_date=payment_date,
                expenditure_type=expenditure_type,
                staff_position=staff_position,
                payment_cost=payment_cost
            )
            messages.success(request, "Salary Allowance created successfully!")
            return redirect('salary_allowance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    salary_allowance = Salary_Allowance.objects.all()
    return render(request, 'salary_allowance.html',{'salary_allowance':salary_allowance})


def update_salary_allowance(request, pk):
    allowance = get_object_or_404(Salary_Allowance, pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        expenditure_type = request.POST.get('expenditure_type')
        staff_position = request.POST.get('staff_position')
        payment_cost = request.POST.get('payment_cost')

        try:
            allowance.name = name
            allowance.payment_date = payment_date
            allowance.expenditure_type = expenditure_type
            allowance.staff_position = staff_position
            allowance.payment_cost = payment_cost
            allowance.save()
            messages.success(request, "Salary Allowance updated successfully!")
            return redirect('salary_allowance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'update_salary_allowance.html', {'allowance': allowance})



def delete_salary_allowance(request, pk):
    allowance = get_object_or_404(Salary_Allowance, pk=pk)
    if request.method == 'POST':
        try:
            allowance.delete()
            messages.success(request, "Salary Allowance deleted successfully!")
            return redirect('salary_allowance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'delete_salary_allowance.html', {'allowance': allowance})

def statutory_deduction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        deduction_type = request.POST.get('deduction_type')
        staff_position = request.POST.get('staff_position')
        payment_cost = request.POST.get('payment_cost')
        try:
            Statutory_Deduction.objects.create(
                name=name,
                payment_date=payment_date,
                deduction_type=deduction_type,
                staff_position=staff_position,
                payment_cost=payment_cost
            )
            messages.success(request, "Salary Allowance created successfully!")
            return redirect('statutory_deduction')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    statutory_deduction = Statutory_Deduction.objects.all()
    return render(request, 'statutory_deduction.html',{'statutory_deduction':statutory_deduction})


def update_statutory_deduction(request, pk):
    allowance = get_object_or_404(Statutory_Deduction, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        deduction_type = request.POST.get('deduction_type')
        staff_position = request.POST.get('staff_position')
        payment_cost = request.POST.get('payment_cost')
        try:
            allowance.name = name
            allowance.payment_date = payment_date
            allowance.deduction_type = deduction_type
            allowance.staff_position = staff_position
            allowance.payment_cost = payment_cost
            allowance.save()
            messages.success(request, "Statutory Deduction updated successfully!")
            return redirect('statutory_deduction')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'update_statutory_deduction.html', {'allowance': allowance})


def delete_statutory_deduction(request, pk):
    allowance = get_object_or_404(Statutory_Deduction, pk=pk)
    if request.method == 'POST':
        try:
            allowance.delete()
            messages.success(request, "Statutory Deduction deleted successfully!")
            return redirect('statutory_deduction')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'delete_statutory_deduction.html', {'allowance': allowance})


def running_cost(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        deduction_type = request.POST.get('deduction_type')
        payment_cost = request.POST.get('payment_cost')
        try:
            Running_Cost.objects.create(
                name=name,
                payment_date=payment_date,
                deduction_type=deduction_type,
                payment_cost=payment_cost
            )
            messages.success(request, "Running Cost created successfully!")
            return redirect('running_cost')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    running_cost = Running_Cost.objects.all()
    return render(request, 'running_cost.html',{'running_cost':running_cost})


def update_running_cost(request, pk):
    allowance = get_object_or_404(Running_Cost, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        deduction_type = request.POST.get('deduction_type')
        payment_cost = request.POST.get('payment_cost')
        try:
            allowance.name = name
            allowance.payment_date = payment_date
            allowance.deduction_type = deduction_type
            allowance.payment_cost = payment_cost
            allowance.save()
            messages.success(request, "Statutory Deduction updated successfully!")
            return redirect('running_cost')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'update_running_cost.html', {'allowance': allowance})


def delete_running_cost(request, pk):
    allowance = get_object_or_404(Running_Cost, pk=pk)
    if request.method == 'POST':
        try:
            allowance.delete()
            messages.success(request, "Running Cost deleted successfully!")
            return redirect('running_cost')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'delete_running_cost.html', {'allowance': allowance})


def president_expenditure(request):
    return render(request, 'president_expenditure.html')


def president_salary_allowance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        expenditure_type = request.POST.get('expenditure_type')
        staff_position = request.POST.get('staff_position')
        payment_cost = request.POST.get('payment_cost')

        try:
            Salary_Allowance.objects.create(
                name=name,
                payment_date=payment_date,
                expenditure_type=expenditure_type,
                staff_position=staff_position,
                payment_cost=payment_cost
            )
            messages.success(request, "Salary Allowance created successfully!")
            return redirect('president_salary_allowance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    president_salary_allowance = Salary_Allowance.objects.all()
    return render(request, 'president_salary_allowance.html',{'president_salary_allowance':president_salary_allowance})



def all_salary_allowance(request):
    salary_allowance = Salary_Allowance.objects.all()
    return render(request, 'all_salary_allowance.html',{'salary_allowance':salary_allowance})


def president_statutory_deduction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        expenditure_type = request.POST.get('expenditure_type')
        staff_position = request.POST.get('staff_position')
        payment_cost = request.POST.get('payment_cost')

        try:
            Statutory_Deduction.objects.create(
                name=name,
                payment_date=payment_date,
                expenditure_type=expenditure_type,
                staff_position=staff_position,
                payment_cost=payment_cost
            )
            messages.success(request, "Statutory Deduction created successfully!")
            return redirect('president_statutory_deduction')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    president_statutory_deduction = Statutory_Deduction.objects.all()
    return render(request, 'president_statutory_deduction.html',{'president_statutory_deduction':president_statutory_deduction})


def all_statutory_deduction(request):
    salary_allowance = Statutory_Deduction.objects.all()
    return render(request, 'all_statutory_deduction.html',{'salary_allowance':salary_allowance})


def president_running_cost(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        deduction_type = request.POST.get('deduction_type')
        payment_cost = request.POST.get('payment_cost')
        try:
            Running_Cost.objects.create(
                name=name,
                payment_date=payment_date,
                deduction_type=deduction_type,
                payment_cost=payment_cost
            )
            messages.success(request, "Running Cost created successfully!")
            return redirect('running_cost')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    president_running_cost = Running_Cost.objects.all()
    return render(request, 'president_running_cost.html',{'president_running_cost':president_running_cost})


def all_running_cost(request):
    salary_allowance = Running_Cost.objects.all()
    return render(request, 'all_running_cost.html',{'salary_allowance':salary_allowance})



from django.db.models import Sum

def salary_allowance_report(request):
    salary_allowance = Salary_Allowance.objects.all()
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        salary_allowance = salary_allowance.filter(payment_date__range=[start_date, end_date])

    total_payment_cost = salary_allowance.aggregate(Sum('payment_cost'))['payment_cost__sum'] or 0

    context = {
        'salary_allowance': salary_allowance,
        'total_payment_cost': total_payment_cost,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'all_salary_allowance.html', context)

def statutory_report(request):
    salary_allowance = Statutory_Deduction.objects.all()
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        salary_allowance = salary_allowance.filter(payment_date__range=[start_date, end_date])

    total_payment_cost = salary_allowance.aggregate(Sum('payment_cost'))['payment_cost__sum'] or 0

    context = {
        'salary_allowance': salary_allowance,
        'total_payment_cost': total_payment_cost,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'all_statutory_deduction.html', context)


def runningcost_report(request):
    salary_allowance = Running_Cost.objects.all()
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        salary_allowance = salary_allowance.filter(payment_date__range=[start_date, end_date])

    total_payment_cost = salary_allowance.aggregate(Sum('payment_cost'))['payment_cost__sum'] or 0

    context = {
        'salary_allowance': salary_allowance,
        'total_payment_cost': total_payment_cost,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'all_running_cost.html', context)



def teacher_expenditure(request):
    return render(request, 'teacher_expenditure.html')



def medical_assistance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        welfare_type = request.POST.get('welfare_type')
        payment_cost = request.POST.get('payment_cost')

        try:
            Medical_Assistance.objects.create(
                name=name,
                payment_date=payment_date,
                welfare_type=welfare_type,
                payment_cost=payment_cost
            )
            messages.success(request, "Medical Allowance created successfully!")
            return redirect('medical_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    medical_assistance = Medical_Assistance.objects.all()
    return render(request, 'medical_assistance.html',{'medical_assistance':medical_assistance})


def update_medical_assistance(request, pk):
    allowance = get_object_or_404(Medical_Assistance, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        welfare_type = request.POST.get('welfare_type')
        payment_cost = request.POST.get('payment_cost')

        try:
            allowance.name = name
            allowance.payment_date = payment_date
            allowance.welfare_type = welfare_type
            allowance.payment_cost = payment_cost
            allowance.save()
            messages.success(request, "Medical Welfare updated successfully!")
            return redirect('medical_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'update_medical_assistance.html', {'allowance': allowance})

def delete_medical_assistance(request, pk):
    allowance = get_object_or_404(Medical_Assistance, pk=pk)
    if request.method == 'POST':
        try:
            allowance.delete()
            messages.success(request, "Medical Allowance deleted successfully!")
            return redirect('medical_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'delete_medical_assistance.html', {'allowance': allowance})


def financial_assistance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        welfare_type = request.POST.get('welfare_type')
        payment_cost = request.POST.get('payment_cost')

        try:
            Financial_Assistance.objects.create(
                name=name,
                payment_date=payment_date,
                welfare_type=welfare_type,
                payment_cost=payment_cost
            )
            messages.success(request, "Financial Allowance created successfully!")
            return redirect('financial_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    financial_assistance = Financial_Assistance.objects.all()
    return render(request, 'financial_assistance.html',{'financial_assistance':financial_assistance})


def update_financial_assistance(request, pk):
    allowance = get_object_or_404(Financial_Assistance, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        welfare_type = request.POST.get('welfare_type')
        payment_cost = request.POST.get('payment_cost')

        try:
            allowance.name = name
            allowance.payment_date = payment_date
            allowance.welfare_type = welfare_type
            allowance.payment_cost = payment_cost
            allowance.save()
            messages.success(request, "Financial Welfare updated successfully!")
            return redirect('financial_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'update_financial_assistance.html', {'allowance': allowance})

def delete_financial_assistance(request, pk):
    allowance = get_object_or_404(Financial_Assistance, pk=pk)
    if request.method == 'POST':
        try:
            allowance.delete()
            messages.success(request, "Financial Allowance deleted successfully!")
            return redirect('financial_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'delete_financial_assistance.html', {'allowance': allowance})


def berievement_assistance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        welfare_type = request.POST.get('welfare_type')
        payment_cost = request.POST.get('payment_cost')

        try:
            Berievement_Assistance.objects.create(
                name=name,
                payment_date=payment_date,
                welfare_type=welfare_type,
                payment_cost=payment_cost
            )
            messages.success(request, "Berievement Allowance created successfully!")
            return redirect('berievement_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    berievement_assistance = Berievement_Assistance.objects.all()
    return render(request, 'berievement_assistance.html',{'berievement_assistance':berievement_assistance})


def update_berievement_assistance(request, pk):
    allowance = get_object_or_404(Berievement_Assistance, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        welfare_type = request.POST.get('welfare_type')
        payment_cost = request.POST.get('payment_cost')

        try:
            allowance.name = name
            allowance.payment_date = payment_date
            allowance.welfare_type = welfare_type
            allowance.payment_cost = payment_cost
            allowance.save()
            messages.success(request, "Berievement Welfare updated successfully!")
            return redirect('berievement_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'update_berievement_assistance.html', {'allowance': allowance})


def delete_berievement_assistance(request, pk):
    allowance = get_object_or_404(Berievement_Assistance, pk=pk)
    if request.method == 'POST':
        try:
            allowance.delete()
            messages.success(request, "Berievement Allowance deleted successfully!")
            return redirect('berievement_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'delete_berievement_assistance.html', {'allowance': allowance})



def education_assistance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        welfare_type = request.POST.get('welfare_type')
        payment_cost = request.POST.get('payment_cost')

        try:
            Education_Assistance.objects.create(
                name=name,
                payment_date=payment_date,
                welfare_type=welfare_type,
                payment_cost=payment_cost
            )
            messages.success(request, "Education Allowance created successfully!")
            return redirect('education_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    education_assistance = Education_Assistance.objects.all()
    return render(request, 'education_assistance.html',{'education_assistance':education_assistance})


def update_education_assistance(request, pk):
    allowance = get_object_or_404(Education_Assistance, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        welfare_type = request.POST.get('welfare_type')
        payment_cost = request.POST.get('payment_cost')

        try:
            allowance.name = name
            allowance.payment_date = payment_date
            allowance.welfare_type = welfare_type
            allowance.payment_cost = payment_cost
            allowance.save()
            messages.success(request, "Eduaction Welfare updated successfully!")
            return redirect('education_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'update_education_assistance.html', {'allowance': allowance})


def delete_education_assistance(request, pk):
    allowance = get_object_or_404(Education_Assistance, pk=pk)
    if request.method == 'POST':
        try:
            allowance.delete()
            messages.success(request, "Education Allowance deleted successfully!")
            return redirect('education_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    return render(request, 'delete_education_assistance.html', {'allowance': allowance})



def president_teacher_expenditure(request):
    return render(request, 'president_teacher_expenditure.html')


def president_medical_assistance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        welfare_type = request.POST.get('welfare_type')
        payment_cost = request.POST.get('payment_cost')

        try:
            Medical_Assistance.objects.create(
                name=name,
                payment_date=payment_date,
                welfare_type=welfare_type,
                payment_cost=payment_cost
            )
            messages.success(request, "Medical Allowance created successfully!")
            return redirect('president_medical_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    president_medical_assistance = Medical_Assistance.objects.all()
    return render(request, 'president_medical_assistance.html',{'president_medical_assistance':president_medical_assistance})


def president_financial_assistance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        welfare_type = request.POST.get('welfare_type')
        payment_cost = request.POST.get('payment_cost')

        try:
            Financial_Assistance.objects.create(
                name=name,
                payment_date=payment_date,
                welfare_type=welfare_type,
                payment_cost=payment_cost
            )
            messages.success(request, "Financial Allowance created successfully!")
            return redirect('president_financial_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    president_financial_assistance = Financial_Assistance.objects.all()
    return render(request, 'president_financial_assistance.html',{'president_financial_assistance':president_financial_assistance})


def president_education_assistance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        welfare_type = request.POST.get('welfare_type')
        payment_cost = request.POST.get('payment_cost')

        try:
            Education_Assistance.objects.create(
                name=name,
                payment_date=payment_date,
                welfare_type=welfare_type,
                payment_cost=payment_cost
            )
            messages.success(request, "Education Allowance created successfully!")
            return redirect('president_education_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    president_education_assistance = Education_Assistance.objects.all()
    return render(request, 'president_education_assistance.html',{'president_education_assistance':president_education_assistance})


def president_medical_assistance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        welfare_type = request.POST.get('welfare_type')
        payment_cost = request.POST.get('payment_cost')

        try:
            Medical_Assistance.objects.create(
                name=name,
                payment_date=payment_date,
                welfare_type=welfare_type,
                payment_cost=payment_cost
            )
            messages.success(request, "Medical Allowance created successfully!")
            return redirect('president_medical_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    president_medical_assistance = Medical_Assistance.objects.all()
    return render(request, 'medical_assistance.html',{'president_medical_assistance':president_medical_assistance})


def president_berievement_assistance(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        payment_date = request.POST.get('payment_date')
        welfare_type = request.POST.get('welfare_type')
        payment_cost = request.POST.get('payment_cost')

        try:
            Berievement_Assistance.objects.create(
                name=name,
                payment_date=payment_date,
                welfare_type=welfare_type,
                payment_cost=payment_cost
            )
            messages.success(request, "Berievement Allowance created successfully!")
            return redirect('president_berievement_assistance')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
    president_berievement_assistance = Berievement_Assistance.objects.all()
    return render(request, 'president_berievement_assistance.html',{'president_berievement_assistance':president_berievement_assistance})