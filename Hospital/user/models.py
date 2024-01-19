from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentProfile(models.Model):
    years_of_studies = models.TextChoices('years_of_studies',['3','4','5'])

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    university_name = models.TextField()
    linkedIn = models.URLField()
    x_link = models.URLField()
    year_of_study = models.CharField(max_length=255,choices=years_of_studies.choices)
    email = models.EmailField()
    cv = models.FileField()
    trascript = models.FileField()
    medical_health = models.FileField()
    bio = models.TextField()

    def __str__(self) -> str:
        return self.user.first_name
    

class Hospital(models.Model):
    students = models.TextChoices('students',['1','2','3','4','5','6','7','8','9','10'])
    deparments = models.TextChoices('deparments',['Surgery','Internal Medicine','Emergency','Orthopedic surgery','Ophthalmology'])

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    depatrtment = models.CharField(max_length=1024)
    training_period = models.TextField()
    number_of_student_need = models.CharField(max_length=1024,choices=students.choices)
    for_contact_number = models.TextField()
    for_contact_email = models.EmailField()
    image = models.ImageField(upload_to='images/')
    def __str__(self) -> str:
        return self.depatrtment


