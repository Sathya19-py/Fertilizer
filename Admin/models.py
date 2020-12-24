from django.db import models

# Create your models here.
class Govt(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    House_Number = models.CharField(max_length=50)
    Village_Name = models.CharField(max_length=50)
    Mandal_Name = models.CharField(max_length=50)
    District_Name = models.CharField(max_length=50)
    State_Name = models.CharField(max_length=50)
    Aadhaar_Number = models.IntegerField()
    PassBook_Number = models.CharField(max_length=20)
    Land = models.DecimalField(max_digits=5,decimal_places=2)