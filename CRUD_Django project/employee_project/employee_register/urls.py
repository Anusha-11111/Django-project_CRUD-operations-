from django.urls import path,include
from.import views

urlpatterns = [
    path('Signup/', views.Signup, name='Signup'),
    path('Login/', views.Login, name='Login'),
    path('base/',views.employee_form,name = 'employee_form'),
    path('list/',views.employee_list,name = "employee_list"),
    path('employee_insert/', views.employee_insert, name='employee_insert'),
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('<int:id>/delete/', views.employee_delete, name='employee_delete'),
]