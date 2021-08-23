from django import forms
from django.db.models import fields
from .models import employee



class EmployeeForm(forms.ModelForm):

    class Meta:
        model = employee
        fields = ('fullname','mobile','emp_code','position')
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'EMP. Code'
        }
