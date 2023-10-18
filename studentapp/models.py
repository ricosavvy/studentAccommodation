from django.db import models

# Import the StudentAcademic model
class StudentAcademic(models.Model):
    student = models.OneToOneField('Student', on_delete=models.CASCADE)
    campus = models.CharField(max_length=100)
    study = models.CharField(max_length=100)
    programme = models.CharField(max_length=100)

class Student(models.Model):

    student_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    date_of_birth = models.DateField()
    nrc = models.CharField(max_length=20)
    nationality = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    town = models.CharField(max_length=100)

    academic_record = models.OneToOneField(StudentAcademic, on_delete=models.CASCADE, related_name='student')
    
    application = models.OneToOneField('Application', on_delete=models.CASCADE, related_name='student', null=True, blank=True)

class Admin(models.Model):
    admin_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    qualifications = models.TextField()
    title = models.CharField(max_length=100)

    rooms_managed = models.ManyToManyField('Room', related_name='admins')
    applications_managed = models.ManyToManyField('Application', related_name='admins')
    students_managed = models.ManyToManyField(Student, related_name='admin')    

class Room(models.Model):
    house_name = models.CharField(max_length=100)
    block_num = models.IntegerField()
    room_num = models.IntegerField()
    available = models.BooleanField()

    class Meta:
        unique_together = ('house_name', 'block_num', 'room_num')

# Application Model
class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    application_date = models.DateField(blank=True, null=True)

class AccommodatedStudent(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE, to_field='room_num')
