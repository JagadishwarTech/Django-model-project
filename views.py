from django.shortcuts import render
from testapp.models import student
def student_list(request):
    student_list = student.objects.all() 
    my_dict={"student_list":student_list}
    return render(request,"testapp/std.html",my_dict)
