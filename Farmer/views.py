from django.shortcuts import render,redirect
from Dealer.models import Product
from Farmer.models import Cart,Order,Customer
from Admin.models import Govt
from django.contrib import messages
import datetime
import random
import string


# Create your views here.
def Home(request):
    return render(request,"home.html")

def ProductHome(request):
    return render(request,"Product.html")

def Single(request):
    if request.method == 'POST':
        Name = request.POST["Name"]
        res = Product.objects.filter(Name=Name)
        if res:
            return render(request,"Farmer/single.html",{"Data":res})
        else:
            messages.info(request,"Product Not Found")
            return redirect("single")
    else:
        Sid = request.GET.get("id")
        res = Product.objects.filter(id=Sid)
        return render(request,"Farmer/single.html",{"Data":res})

def Registration(request):
    if request.method == 'POST':
        First_Name = request.POST['fname']
        Last_Name = request.POST['lname']
        Mobile_Number = request.POST['mobile']
        Email_Id = request.POST['email']
        House_Number = request.POST['houseno']
        Village_Name = request.POST['village']
        Mandal_Name = request.POST['mandal']
        District_Name = request.POST['district']
        State_Name = request.POST['state']
        Aadhaar_Number = request.POST['aadhaar']
        PassBook_Number = request.POST['passbook']
        Land = request.POST['land']
        Password = request.POST['password']
        Password1 = request.POST['password1']

        
        
        if Customer.objects.filter(Aadhaar_Number=Aadhaar_Number).exists():
            messages.info(request,"Cridentials already Available")
            return redirect("registration")
        elif Customer.objects.filter(Email_Id=Email_Id).exists():
            messages.info(request,"Email Id is Alredy exists..")
            return redirect("registration")
        elif Customer.objects.filter(Mobile_Number=Mobile_Number).exists():
            messages.info(request,"Mobile Number is Alredy exists..")
            return redirect("registration")
        else:
            if Password == Password1:
                if Govt.objects.filter(Aadhaar_Number=Aadhaar_Number).exists():
                    res = Govt.objects.filter(Aadhaar_Number=Aadhaar_Number)
                    for x in res:
                        fname = x.First_Name
                        lname = x.Last_Name
                        hno = x.House_Number
                        vname = x.Village_Name
                        mname = x.Mandal_Name
                        dname = x.District_Name
                        ano = x.Aadhaar_Number
                        pno = x.PassBook_Number
                        landing = x.Land
                        land = str(landing)

                        print(fname)
                        print(lname)
                        print(ano)
                        print(landing)
                        print(type(landing))

                        print(land)
                        print(type(land))
                    
                        
                        if First_Name == fname:
                            if Last_Name == lname:
                                if House_Number == hno:
                                    if Village_Name == vname:
                                        if Mandal_Name == mname:
                                            if District_Name == dname:
                                                if PassBook_Number == pno:
                                                    if Land == land:
                                                        New_Customer = Customer(First_Name=First_Name,Last_Name=Last_Name,Mobile_Number=Mobile_Number,
                                                        Email_Id=Email_Id,House_Number=House_Number,Village_Name=Village_Name,Mandal_Name=Mandal_Name,
                                                        District_Name=District_Name,State_Name=State_Name,Aadhaar_Number=Aadhaar_Number,PassBook_Number=PassBook_Number,
                                                        Land=Land,Password=Password)
                                                        New_Customer.save()
                                                        messages.info(request,"Your Application Successfully Submitted")
                                                        return redirect("registration")
                                                    else:
                                                        messages.info(request,"Land Details Are Not Matching As Govt Details")
                                                        return redirect("registration")
                                                else:
                                                    messages.info(request,"PassBook Number is Not Matching As Govt Deatails")
                                                    return redirect("registration")
                                            else:
                                                messages.info(request,"District Name is Not Matching As Govt Deatails")
                                                return redirect("registration")
                                        else:
                                            messages.info(request,"Mandal Name is Not Matching As Govt Deatails")
                                            return redirect("registration")
                                    else:
                                        messages.info(request,"Village Name is Not Matching As Govt Deatails")
                                        return redirect("registration")
                                else:
                                    messages.info(request,"House Number is Not Matching As Govt Deatails")
                                    return redirect("registration")
                            else:
                                messages.info(request,"Last Name is Not Matching As Govt Deatails")
                                return redirect("registration")
                        else:
                            messages.info(request,"First Name is Not Matching As Govt Deatails")
                            return redirect("registration")
                else:
                    messages.info(request,"Aadhaar Number is Not Matching As Govt Deatails")
                    return redirect("registration")
            else:
                messages.info(request,"password not matching...")
                return redirect("registration")
    else:
        return render(request,"Registration.html")

def CustLogin(request):
    return render(request,"customer login.html")

def Contact(request):
    return render(request,"contact us.html")

def Track(request):
    return render(request,"Track.html")

def Farmer_Home(request):
    return render(request,"Farmer/Farmer Home.html")



def Farmer_Product(request):
    new = Product.objects.all()
    count = 0
    for item in Cart.objects.all():
        count += 1
    return render(request,"Farmer/Farmer Product.html",{"pro":new,"c":count})

def AddCart(request):
    if request.method == "POST":
        p_no = request.POST["id"]
        Name = request.POST["Name"]
        Price = int(request.POST["Price"])
        Weight = int(request.POST["Weight"])
        Weight1 = request.POST["Weight1"]
        Image = request.POST['Image']
        Quantity = int(request.POST["Quantity"])
        Sub_Total = Price * Quantity
        print(Sub_Total)

        if Cart.objects.filter(Index_Id=p_no).exists():
            messages.info(request,'Product Already exist in Cart')
            return redirect('fproduct')
        
        else:
            Cart(Index_Id=p_no,Name=Name,Price=Price,Weight=Weight,Weight1=Weight1,Image=Image,Quantity=Quantity,Sub_Total=Sub_Total).save()

            Add = Product.objects.all()
            count = 0
            for item in Cart.objects.all():
                count += 1
            return render(request,"Farmer/Farmer Product.html",{"pro":Add,"c":count})
    else:
        count = 0
        for item in Cart.objects.all():
            count += 1
        return redirect('fproduct',{"c":count})


def Farmer_Cart(request):
    count = 0
    Total = 0
    for item in Cart.objects.all():
        Total += item.Sub_Total
        count += 1
    New = Cart.objects.all()
    return render(request,"Farmer/Farmer Cart.html",{"car":New,'t':Total,"c":count})

def DeleteCart(request):
    Cid = request.GET.get("Id")
    Cart.objects.filter(Index_Id=Cid).delete()
    return redirect("fcart")

def CheckOut(request):
    Total = 0
    if request.method == "POST":
        Total = request.POST["Total"]
    res = Cart.objects.all()
    return render(request,"Farmer/Checkout.html",{"car":res,"t":Total})
    

def Farmer_Orders(request):
    if request.method == "POST":
        Price = 0
        Image = 0
        Name = 0
        Quantity = 0
        Payment = request.POST.get("Payment")
        for item in Cart.objects.all():
            id = item.Index_Id
            Name = item.Name
            Price = item.Sub_Total
            Image = item.Image
            Quantity = item.Quantity
        d = datetime.date.today()
        Delivery_Date = datetime.date.today() + datetime.timedelta(days=5)
        print(Delivery_Date)
        print(d)
        def Oid():
            x = random.randrange(1000000000,9999999999)
            print(x)
            i = "OD"
            n = str(i)
            r = (n + str(x))
            num = str(r)
            print(num)
            try :
                order = Order.objects.get(Order_Id=num)
                Oid()
            except Order.DoesNotExist:
                return num
        Order_Id = Oid()
        Order(Name=Name,Price=Price,Image=Image,Quantity=Quantity,Order_Id=Order_Id,Order_Date=d,Payment_Mode=Payment,Delivery_Date=Delivery_Date).save()
        Cart.objects.all().delete()
        res = Order.objects.all()
        return render(request,"Farmer/Farmer Orders.html",{"ord":res})
    else:
        res = Order.objects.all()
        return render(request,"Farmer/Farmer Orders.html",{"ord":res})

def Order_Details(request):
    if request.method == 'POST':
        id = request.POST.get("OID")
        res = Order.objects.filter(Order_Id=id)
        if res:
            return render(request,"Farmer/Order Details.html",{"Data":res})
        else:
            messages.info(request,'Order Details Not Found')
            return redirect("ftrack")
    else:
        Did = request.GET.get("id")
        res = Order.objects.filter(id=Did)
        return render(request,"Farmer/Order Details.html",{"Data":res})

def Farmer_Notifications(request):
    return render(request,"Farmer/Farmer Notifications.html")

def Farmer_Track(request):
    return render(request,"Farmer/Farmer Track.html")

def Farmer_Info(request):
    return render(request,"Farmer/Farmer Info.html")

def Tracking(request):
    if request.method == 'POST':
        id = request.POST.get("OID")
        res = Order.objects.filter(Order_Id=id)
        return render(request,"Tracking.html",{"Data":res})

def FAddress(request):
    return render(request,"Farmer/Farmer Address.html")

def AddAddress(request):
    return render(request,"Farmer/Add Address.html")