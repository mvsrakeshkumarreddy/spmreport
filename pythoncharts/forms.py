from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()




class DateInput(forms.DateInput):
    input_type = 'date'

class RegisterUserForm(UserCreationForm):
    full_name = forms.CharField(max_length = 150, required=True)

    crew_ID = forms.CharField(max_length = 7)
    station = forms.CharField(max_length = 3) 
    employee_ID = forms.CharField(max_length = 11)
    #full_name = forms.CharField(max_length = 150)
    first_name = forms.CharField(max_length = 150)
    last_name = forms.CharField(max_length = 150)
    email = forms.EmailField()
    #appointment_date = forms.DateField(widget = forms.SelectDateWidget(years=range(1995, 2050)))
    appointment_date = forms.DateInput()
    #employee_ID = forms.DateField(widget = forms.SelectDateWidget)
    #employee_ID  = forms.CharField(max_length = 11)
    #appdate = forms.DateField(widget = forms.SelectDateWidget)   

    class Meta:
        model = User
        widgets = {
            'appointment_date': DateInput(),
        }

        fields = ('full_name', 'crew_ID', 'station','employee_ID', 'appointment_date', 'first_name', 'last_name', 'email', 'password1', 'password2')
        """, 'employee_ID', 'appdate', 'station', 'password1', 'password2')"""