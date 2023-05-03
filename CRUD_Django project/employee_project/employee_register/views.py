from django.shortcuts import render,redirect, get_object_or_404
from.forms import EmployeeForm
from .models import Employee
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def Signup(request):
    if request.method == "POST":
        Firstname = request.POST["Firstname"]
        Lastname = request.POST["Lastname"]
        email = request.POST["email"]
        password = request.POST["password"]

        myuser = User.objects.create_user(username=email, password=password)
        myuser.first_name = Firstname
        myuser.last_name = Lastname
        myuser.save()

        messages.success(request, "Your account has been successfully created")

        return redirect("Login")
    return render(request, "employee_register/Signup.html")


def Login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("base")

        else:
            messages.error(request, "Wrong credentials!")
            return redirect(reverse("Signup"))

    return render(request, "employee_register/Login.html")



def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)

def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_insert(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmployeeForm()

    context = {'form': form}
    return render(request, 'employee_register/employee_form.html', context)

def employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee_register/employee_form.html', {'form': form})

def employee_delete(request, id):
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return redirect('employee_list')