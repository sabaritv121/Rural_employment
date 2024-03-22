from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login_view(AbstractUser):
    is_users = models.BooleanField(default=False)
    is_panchayath = models.BooleanField(default=False)


class users(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE,related_name='user')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    adhar_number = models.CharField(max_length=16)
    Resume = models.FileField(upload_to='Resume/')

    def __str__(self):
        return self.name




class Panchayath(models.Model):
    user=models.ForeignKey(Login_view,on_delete=models.CASCADE,related_name="panchayath")
    panchayath_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.panchayath_name




class Notification(models.Model):
    message= models.CharField(max_length=100)
    date = models.DateField(auto_now=True)


class AddScheme(models.Model):
    scheme_name =  models.CharField(max_length=100)
    scheme_fund = models.CharField(max_length=100)
    scheme_tenure = models.CharField(max_length=100)

    def __str__(self):
        return self.scheme_name


class Complaints(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.DO_NOTHING)
    feedback = models.TextField()
    date = models.DateField(auto_now=True)
    reply = models.TextField(null=True, blank=True)



class AppointmentSchedule(models.Model):
    QUALIFICATION_CHOICES = (
        ('high_school', 'High School'),
        ('Degree', 'Degree'),
        ('masters', 'Master\'s Degree'),
        ('phd', 'PhD'),
    )
    user = models.ForeignKey(Panchayath, on_delete=models.DO_NOTHING)
    scheme = models.ForeignKey(AddScheme, on_delete=models.DO_NOTHING)
    qualifications = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()

    designation = models.CharField(max_length=50)



class Appointment(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(AppointmentSchedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)


