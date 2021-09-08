from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import employee
# Create your views here.

def employee_list(request):
    context = {'employee_list': employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)

def employee_form(request):
    if request.method == 'GET':
        form = EmployeeForm()
        return render(request,'employee_register/employee_form.html',{'form':form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_delete(request):
    return