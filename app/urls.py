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




]

