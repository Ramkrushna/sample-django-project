from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        address = request.POST['address']
        
        Student.objects.create(name=name, age=age, email=email, address=address)
        messages.success(request, "Student Added Successfully!")
        return redirect('list_students')
    return render(request, 'students_app/add_student.html')


def update_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.email = request.POST['email']
        student.address = request.POST['address']
        student.save()
        messages.success(request, "Student Updated Successfully!")
        return redirect('list_students')
    return render(request, 'students_app/update_student.html', {'student': student})


def list_students(request):
    students = Student.objects.all()
    return render(request, 'students_app/list_students.html', {'students': students})


def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    messages.success(request, "Student Deleted Successfully!")
    return redirect('list_students')


def about(request):
    return render(request, 'students_app/about.html')
