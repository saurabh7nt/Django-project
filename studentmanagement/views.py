from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
from .models import Student

# def index(request):
#     return render(request, 'index.html')

def student_home(request):
    return render(request, "home.html", {})
    # return HttpResponse("<h1>Hello World</h1>")


# This decorator will exempt the specified view from CSRF protection, allowing requests to be processed without the required CSRF tokens.
@csrf_exempt                            
def add_student(request):
    if request.method=="POST":
        # print("working")

        #step1: Fetching
        name=request.POST.get("name")
        rollno=request.POST.get("rollno")
        age=request.POST.get("age")
        std=request.POST.get("std")
        email=request.POST.get("email")
        address=request.POST.get("address")

        #step2 : creating model object and set the data
        s=Student()
        s.name=name
        s.rollno=rollno
        s.age=age
        s.address=address
        s.email=email
        s.std=std

        # step3 : savind data
        s.save()
        return redirect("/student/show")
    return render(request, "add-student.html", {})

@csrf_exempt
def show_student(request):
    studs=Student.objects.all()
    return render(request, 'show-students.html', {
        'studs':studs
    })


def delete_student(request, rollno):
    # print(rollno)
    stu=Student.objects.get(rollno=rollno)
    stu.delete()
    return redirect("/student/show/")

# def update_student(request, rollno):
#     # print(rollno)
#     stu=Student.objects.get(rollno=rollno)
#     return redirect(request, "update-student.html",{
#         'stu':stu
#     })
