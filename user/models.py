from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import uuid


class LoginUser(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=10)
    usertype=models.CharField(max_length=20)

class Provider(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=25,unique=True)
    phone=models.CharField(max_length=13)
    address=models.TextField()
    vehicle_name=models.CharField(max_length=40)
    vehicle_number=models.CharField(max_length=15)
    year=models.CharField(max_length=5)
    date_joined=models.CharField(max_length=10)
    is_active=models.BooleanField(default=True)
    provider_img=models.FileField(upload_to="")
    vehicle_img=models.FileField(upload_to="")

class Registration(models.Model):
    fullname = models.CharField(max_length=255) 
    emailid = models.EmailField(unique=True)  
    password = models.CharField(max_length=20, default='default_value')
    mob_number = models.CharField(max_length=15)  
    licensenumber = models.CharField(max_length=100) 
    licensepic = models.FileField(upload_to="")  
    userpic = models.FileField(upload_to="") 
    signpic = models.FileField(upload_to="")  
    date_registered = models.DateTimeField(auto_now_add=True)


class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="")  

def vehicle_id(self):
        return f"V{self.id}"

class BookVehicle(models.Model):
    name = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.FileField(upload_to="")

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

def generate_booking_id():
   
    return uuid.uuid4().hex[:8].upper()

class Booking(models.Model):
    booking_type_choices = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]
    booking_id = models.CharField(max_length=20, unique=True, editable=False, default=generate_booking_id)
    name = models.CharField(max_length=100, default = 'Default Value')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    booking_type = models.CharField(max_length=10, choices=booking_type_choices, null=False, blank=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True) 
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    dropoff_date = models.DateField()
    dropoff_time = models.TimeField()
    duration = models.PositiveIntegerField(default=0) 
    base_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    taxes = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    
    
    def __str__(self):
        return f"{self.booking_type.capitalize()} Booking from {self.pickup_date} to {self.dropoff_date}"
    



    

