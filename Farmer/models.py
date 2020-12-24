from django.db import models
import datetime

# Create your models here.

class Customer(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Mobile_Number = models.IntegerField()
    Email_Id = models.EmailField(max_length=20)
    House_Number = models.CharField(max_length=50)
    Village_Name = models.CharField(max_length=50)
    Mandal_Name = models.CharField(max_length=50)
    District_Name = models.CharField(max_length=50)
    State_Name = models.CharField(max_length=50)
    Aadhaar_Number = models.IntegerField()
    PassBook_Number = models.CharField(max_length=50)
    Land = models.DecimalField(max_digits=10,decimal_places=2)
    Password = models.CharField(max_length=20)

class Cart(models.Model):
    Index_Id = models.IntegerField(default=0)
    Email = models.EmailField(max_length=100,default=0)
    Name = models.CharField(max_length=20)
    Price = models.IntegerField()
    Image = models.ImageField(upload_to='cart')
    Quantity = models.IntegerField()
    Weight = models.IntegerField(default=0)
    Weight1 = models.CharField(max_length=20)
    Sub_Total = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

class Order(models.Model):
    Index_Id = models.IntegerField(default=0)
    Email = models.EmailField(max_length=100,default=0)
    Name = models.CharField(default="ABC",max_length=100)
    Image = models.ImageField(upload_to='orders')
    Price = models.IntegerField(default=0)
    Order_Id = models.CharField(max_length=50,default="ABC",unique=True)
    Order_Status = models.CharField(default=0,max_length=100)
    Quantity = models.IntegerField(default=0)
    Payment_Mode = models.CharField(default=0,max_length=100)
    Payment_Status = models.CharField(default=0,max_length=100)
    Delivery_Address = models.TextField(default=0)
    Order_Date = models.DateField(auto_now=True)
    Delivery_Date = models.DateField(blank=True, null=True)
    