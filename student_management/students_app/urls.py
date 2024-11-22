from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_student, name='add_student'),
    path('update/<int:student_id>/', views.update_student, name='update_student'),
    path('list/', views.list_students, name='list_students'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('about/', views.about, name='about'),
]
