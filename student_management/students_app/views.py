from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
from .forms import ContactForm


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


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Example: print to console or save to a database
            print(f"Message from {name} <{email}>: {message}")
            messages.success(request, "Form submitted Successfully!")
            # Redirect or display a success message
            return redirect('list_students')
    else:
        form = ContactForm()

    return render(request, 'students_app/contact.html', {'form': form})
