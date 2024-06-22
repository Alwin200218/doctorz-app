from django.db import models

# Create your models here.


class Userdata(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


    def __str__(self):
        return self.email
    
class Doctorinfo(models.Model):
    doctor_image=models.ImageField(upload_to="doctors/")  
    doctor_name = models.CharField(max_length=100)
    doctor_spec = models.CharField(max_length=100)

    def __str__(self):
        return self.doctor_name    
    


class Appointmentinfo(models.Model):
    doctor=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    age = models.IntegerField()
    email= models.CharField(max_length=100)
    contactno=models.IntegerField()
    desc=models.TextField() 

    def __str__(self):
        return self.name    
