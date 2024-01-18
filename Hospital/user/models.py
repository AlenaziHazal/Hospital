from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    university_name = models.TextField()
    year_of_study = models.DateField()
    email = models.EmailField()
    cv = models.FileField()
    trascript = models.FileField()
    medical_health = models.FileField()
    def __str__(self) -> str:
        return self.user.first_name


