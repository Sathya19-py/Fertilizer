from django.shortcuts import render,redirect
from Dealer.models import Product,Seller
from Farmer.models import Order
from django.contrib import messages
import string
import random

from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from Dealer.serializers import ProductSerializer,Product

class ProductOperations(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReadProducts(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer





# Create your views here.
def SellWithUs(request):
    if request.method == 'POST':
        Full_Name = request.POST['Name']
        Email_Id = request.POST['Email']
        Mobile_No = request.POST['Mobile']
        Shop_Name = request.POST['ShopName']
        Shop_Id = request.POST['ShopId']
        Address = request.POST['Address']

        def password():
            size = 10
            chars= string.ascii_uppercase + string.digits
            the_Id = "".join(random.choice(chars) for x in range(size))
            print(the_Id)
            try :
                spass = Seller.objects.get(Password = the_Id)
                password()
            except Seller.DoesNotExist:
                return the_Id
        Password = password()
            
        
        if Seller.objects.filter(Email_Id=Email_Id).exists():
            messages.info(request,"Email id is already available...")
            return redirect("sell_with")
        elif Seller.objects.filter(Mobile_No=Mobile_No).exists():
            messages.info(request,"Mobile Number is already available...")
            return redirect("sell_with")
        elif Seller.objects.filter(Shop_Name=Shop_Name).exists():
            messages.info(request,"Shop Name is already available...")
            return redirect("sell_with")
        elif Seller.objects.filter(Shop_Id=Shop_Id).exists():
            messages.info(request,"Shop Id is already available...")
            return redirect("sell_with")
        else:
            New_Seller = Seller(Full_Name=Full_Name,Email_Id=Email_Id,Mobile_No=Mobile_No,Shop_Name=Shop_Name,
            Shop_Id=Shop_Id,Password=Password,Address=Address)
            New_Seller.save()
            messages.info(request,"Your Registration completed successfully...")
            return redirect("sell_with")
    else:
        return render(request,"sell with us.html")

def SellLogin(request):
    return render(request,"Seller Login.html")

def Home(request):
    return render(request,"Dealer/Dealer Home.html")

def Add_Product(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Price = request.POST['Price']
        Quantity = request.POST['Quantity']
        Weight = request.POST['Weight']
        Weight1 = request.POST['Weight1']
        Description = request.POST['Description']
        Image = request.FILES['Image']
        New = Product(Name=Name,Price=Price,Quantity=Quantity,Weight=Weight,Weight1=Weight1,Description=Description,Image=Image)
        New.save()
        messages.info(request,"Product Added Successfully")
        return redirect('add')
    else:
        return render(request,"Dealer/Add Product.html")

def Delete_Update(request):
    res = Product.objects.all()
    return render(request,"Dealer/Delete and Update Product.html",{"pro":res})


def Update(request):
    uid = request.POST.get("id")
    res = Product.objects.get(id=uid)
    return render(request,"Dealer/Update Product.html",{"data":res})

def Update_Product(request):
    id = request.POST["id"]
    Name = request.POST["Name"]
    Price = request.POST["Price"]
    Quantity = request.POST["Quantity"]
    Weight = request.POST["Weight"]
    Weight1 = request.POST["Weight1"]
    Product.objects.filter(id=id).update(Name=Name,Price=Price,Quantity=Quantity,Weight=Weight,Weight1=Weight1)
    return Delete_Update(request)

def Delete(request):
    Did = request.GET['id']
    Product.objects.filter(id=Did).delete()
    return redirect("delete_and_update")

def Orders(request):
    res = Order.objects.all()
    return render(request,"Dealer/Order Received.html",{"Data":res})

def Delivery_Status(request):
    return render(request,"Dealer/Delivery Status.html")