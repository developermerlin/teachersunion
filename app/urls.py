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









]

