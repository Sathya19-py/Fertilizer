from django.db import models

# Create your models here.
class Seller(models.Model):
    Full_Name = models.CharField(max_length=50)
    Email_Id = models.EmailField(max_length=120)
    Mobile_No = models.IntegerField()
    Shop_Name = models.CharField(max_length=100)
    Shop_Id = models.CharField(max_length=100)
    Password = models.CharField(max_length=20,blank=True)
    Address = models.TextField(max_length=200)
    


class Product(models.Model):
    Name = models.CharField(max_length=20)
    Unique_Id = models.IntegerField(default=False)
    Email = models.EmailField(max_length=100,default=0)
    Price = models.IntegerField()
    Description = models.TextField()
    Quantity = models.IntegerField()
    Weight = models.IntegerField()
    Weight1 = models.CharField(max_length=10)
    Image = models.ImageField(upload_to='Products')
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)