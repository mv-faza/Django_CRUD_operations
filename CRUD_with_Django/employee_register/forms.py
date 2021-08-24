from django import forms
from .models import employee



class EmployeeForm(forms.ModelForm):

    class Meta:
        model = employee
        fields = ('fullname','mobile','emp_code','position')
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'EMP. Code'
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "select"
        self.fields['emp_code'].required = False