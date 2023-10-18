from django.contrib import admin
from .models import Student, StudentAcademic, Application, Room, Admin, AccommodatedStudent
# Register your models here.
admin.site.register(Student)
admin.site.register(StudentAcademic)
admin.site.register(Application)
admin.site.register(Room)
admin.site.register(Admin)
admin.site.register(AccommodatedStudent)