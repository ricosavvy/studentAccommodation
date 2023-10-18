from datetime import date
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Student, StudentAcademic, Application, Room, Admin, AccommodatedStudent
from .forms import RoomForm, ApplicationForm


# Create your views here.
def home(request):
    return render(request, 'home.html')
def student_dashboard(request):
    student = Student.objects.get(student_id=request.user.student_id)  # Assuming you have user authentication in place
    academic_info = StudentAcademic.objects.get(student=student)
    return render(request, "student_dashboard.html", {"student": student, "academic_info": academic_info})
def my_accommodation(request):
    student_id = request.user.student_id  # Assuming you have user authentication
    try:
        assigned_room = AccommodatedStudent.objects.get(student_id=student_id).room
    except AccommodatedStudent.DoesNotExist:
        assigned_room = None

    return render(request, 'my_accommodation.html', {"assigned_room": assigned_room})
# My Application view
def my_application(request):
     if request.method == 'POST':
        # Process the submitted application form
        form = ApplicationForm(request.POST)
        if form.is_valid():
            # Create a new Application instance with the form data
            new_application = form.save(commit=False)
            
            # Associate the application with the current student
            new_application.student = request.user.student  # Assuming you have user authentication in place
            
            # Save the application to the database
            new_application.save()
            
            return HttpResponse("Application submitted successfully")
     else:
        form = ApplicationForm()

     return render(request, "my_application.html", {"form": form})
# Notifications view
def notifications(request):
    return render(request, 'notifications.html')

# Profile view
def stu_profile(request):
    return render(request, 'Stu_profile.html')

# Logout view (simple example that logs the user out)
def logout(request):
    # You may want to implement a more secure logout process
    return HttpResponse("You have been logged out.")
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

def manage_rooms(request):
    rooms = Room.objects.all()
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_rooms')
    return render(request, 'manage_rooms.html', {'rooms': rooms, 'form': form})   
def manage_students(request):
    return render(request, "manage_students.html")

def manage_applications(request):
     # Query the database to retrieve all submitted applications
    applications = Application.objects.all()

    return render(request, "manage_applications.html", {"applications": applications})

def manage_accommodation(request):
    accommodated_students = AccommodatedStudent.objects.all()
    return render(request, "manage_accommodation.html", {"accommodated_students": accommodated_students})
def admin_profile(request):
    return render(request, "admin_profile.html")

from django.shortcuts import render, get_object_or_404, redirect
from .models import Room
from .forms import RoomForm

def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_rooms')

    form = RoomForm()
    return render(request, 'create_room.html', {'form': form})

def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('manage_rooms')

    form = RoomForm(instance=room)
    return render(request, 'edit_room.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect
from .models import Room

def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        room.delete()
        return redirect('manage_rooms')

    return render(request, 'delete_room.html', {'room': room})

