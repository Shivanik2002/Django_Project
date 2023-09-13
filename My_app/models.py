from django.db import models

# Create your models here.

class Register(models.Model):
    First_Name=models.CharField(max_length=50)
    Middle_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Phone_Name=models.CharField(max_length=15)
    College_Name=models.CharField(max_length=100)
    Home_Address=models.CharField(max_length=50)
    Gender=models.CharField(max_length=10)
    Area_of_Intrest=models.CharField(max_length=100)

    def __str__(self):
        return self.First_Name
