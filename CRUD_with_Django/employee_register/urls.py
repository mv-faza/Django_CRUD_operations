from django.urls import path
from . import views 

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),   # get and post
    path('<int:id>/', views.employee_form,name='employee_update'),     #get and post
    path('delete/<int:id>/',views.employee_delete,name='employee_delete' ),
    path('list/', views.employee_list, name='employee_list'),      # get
]