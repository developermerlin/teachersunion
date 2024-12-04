from django.urls import path
from . import views


urlpatterns = [
    path('', views.home1, name='home1'),
    path('secretary/', views.secretary, name='secretary'),
    path('finance/', views.finance, name='finance'),
    path('president/', views.president, name='president'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/edit/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('teacher/delete/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    path('teacher/<int:teacher_id>/', views.teacher_details, name='teacher_details'), 

    path('finance_teachers/', views.finance_teachers, name='finance_teachers'),
    path('finance_teachers_details/<int:teacher_id>/', views.finance_teachers_details, name='finance_teachers_details'),
    
    path('budget/', views.budget, name='budget'),
    path('edit_budget/edit/<int:budget_id>/', views.edit_budget, name='edit_budget'),
    path('budget/<int:budget_id>/', views.budget_details, name='budget_details'), 

    path('president_budget/', views.president_budget, name='president_budget'),
    path('president_budget_details/<int:budget_id>/', views.president_budget_details, name='president_budget_details'), 
    path('president_teachers/', views.president_teachers, name='president_teachers'),
    path('president_teachers_details/<int:teacher_id>/', views.president_teachers_details, name='president_teachers_details'),

    path('president_messages/', views.president_messages, name='president_messages'),
    path('edit_president_messages/<int:president_id>/', views.edit_president_messages, name='edit_president_messages'),
    path('delete_president_message/delete/<int:president_id>/', views.delete_president_message, name='delete_president_message'),
    path('president_message_details/<int:teacher_id>/', views.president_message_details, name='president_message_details'),

    path('finance_messages/', views.finance_messages, name='finance_messages'),
    path('view_president_message_details/<int:teacher_id>/', views.view_president_message_details, name='view_president_message_details'),

    path('message_to_president/', views.message_to_president, name='message_to_president'),
    path('edit_message_to_president/<int:president_id>/', views.edit_message_to_president, name='edit_message_to_president'),
    path('delete_message_to_president/delete/<int:president_id>/', views.delete_message_to_president, name='delete_message_to_president'),

    path('message_from_finance/', views.message_from_finance, name='message_from_finance'),
    path('view_message_from_finance/<int:teacher_id>/', views.view_message_from_finance, name='view_message_from_finance'),

    path('admin_expenditure/', views.admin_expenditure, name='admin_expenditure'),
    path('salary_allowance/',views.salary_allowance, name='salary_allowance'),
    path('allowances/<int:pk>/update/', views.update_salary_allowance, name='update_salary_allowance'),
    path('allowances/<int:pk>/delete/', views.delete_salary_allowance, name='delete_salary_allowance'),


    path('statutory_deduction/',views.statutory_deduction, name='statutory_deduction'),
    path('deduction/<int:pk>/update/', views.update_statutory_deduction, name='update_statutory_deduction'),
    path('deduction/<int:pk>/delete/', views.delete_statutory_deduction, name='delete_statutory_deduction'),

    path('running_cost/',views.running_cost, name='running_cost'),
    path('running_cost/<int:pk>/update/', views.update_running_cost, name='update_running_cost'),
    path('running_cost/<int:pk>/delete/', views.delete_running_cost, name='delete_running_cost'),


    path('president_expenditure/', views.president_expenditure, name='president_expenditure'),
    path('president_salary_allowance/',views.president_salary_allowance, name='president_salary_allowance'),
    path('president_statutory_deduction/',views.president_statutory_deduction, name='president_statutory_deduction'),
    path('president_running_cost/',views.president_running_cost, name='president_running_cost'),
    

    path('all_salary_allowance/', views.all_salary_allowance, name='all_salary_allowance'),
    path('all_statutory_deduction/', views.all_statutory_deduction, name='all_statutory_deduction'),
    path('all_running_cost/', views.all_running_cost, name='all_running_cost'),


    path('salary-allowance-report/', views.salary_allowance_report, name='salary_allowance_report'),
    path('statutory_report/', views.statutory_report, name='statutory_report'),
    path('runningcost_report/', views.runningcost_report, name='runningcost_report'),


    path('teacher_expenditure/', views.teacher_expenditure, name='teacher_expenditure'),

    path('medical_assistance/', views.medical_assistance, name='medical_assistance'),
    path('medical/<int:pk>/update/', views.update_medical_assistance, name='update_medical_assistance'),
    path('medical/<int:pk>/delete/', views.delete_medical_assistance, name='delete_medical_assistance'),



    path('financial_assistance/', views.financial_assistance, name='financial_assistance'),
    path('financial/<int:pk>/update/', views.update_financial_assistance, name='update_financial_assistance'),
    path('financial/<int:pk>/delete/', views.delete_financial_assistance, name='delete_financial_assistance'),
 

    path('berievement_assistance/', views.berievement_assistance, name='berievement_assistance'),
    path('berievement/<int:pk>/update/', views.update_berievement_assistance, name='update_berievement_assistance'),
    path('berievement/<int:pk>/delete/', views.delete_berievement_assistance, name='delete_berievement_assistance'),


    path('education_assistance/', views.education_assistance, name='education_assistance'),
    path('education/<int:pk>/update/', views.update_education_assistance, name='update_education_assistance'),
    path('education/<int:pk>/delete/', views.delete_education_assistance, name='delete_education_assistance'),



]

