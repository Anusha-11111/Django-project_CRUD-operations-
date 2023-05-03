from django import forms
from .models import Employee
from .models import Signup
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Signup
        fields = ('Fisrtname', 'Lastname', 'email', 'password')
        labels = {
            'Fisrtname': 'First Name',
            'Lastname': 'Last Name',
            'password': 'Password',
        }

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', required=True)

    class Meta:
        model = Signup
        fields = ('email', 'password')
        labels = {
            'email': 'Email',
            'password': 'Password',
        }


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','mobile','emp_code','position')
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False
