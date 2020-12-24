from django.shortcuts import render,redirect
from django.contrib import messages
from Dealer.models import Seller
from Admin.models import Govt
from Farmer.models import Customer

def Admin_Login(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        password = request.POST["password"]
        if uname == admin or password == admin:
            return render(request,"Farmer Data.html")
        else:
            messages.info(request,"uname and password is admin")
            return redirect('alogin')
    else:
        return render(request,"Admin Login.html")

def Farmer_Data(request):
    res = Customer.objects.all()
    return render(request,"Farmer Data.html",{"data":res})

def Dealer_Data(request):
    sell = Seller.objects.all()
    return render(request,"Dealer Data.html",{"s":sell})

def Govt_Data(request):
    data = Govt.objects.all()
    return render(request,"Govt DB.html",{"i":data})

def Govt_Add_Farmer(request):
    if request.method == "POST":
        First_Name = request.POST['fname']
        Last_Name = request.POST['lname']
        House_Number = request.POST['houseno']
        Village_Name = request.POST['village']
        Mandal_Name = request.POST['mandal']
        District_Name = request.POST['district']
        State_Name = request.POST['state']
        Aadhaar_Number = request.POST['aadhaar']
        PassBook_Number = request.POST['passbook']
        Land = request.POST['land']

        if Govt.objects.filter(Aadhaar_Number=Aadhaar_Number).exists():
            messages.info(request,"Aadhaar Number is already Available...")
            return redirect("govtaddfarmer")
        elif Govt.objects.filter(PassBook_Number=PassBook_Number).exists():
            messages.info(request,"PassBook Number is already Available...")
            return redirect("govtaddfarmer")
        else:
            New_Farmer = Govt(First_Name=First_Name,Last_Name=Last_Name,House_Number=House_Number,Village_Name=Village_Name,
                        Mandal_Name=Mandal_Name,District_Name=District_Name,State_Name=State_Name,Aadhaar_Number=Aadhaar_Number,
                        PassBook_Number=PassBook_Number,Land=Land)
            New_Farmer.save()
            return redirect("gdata")      
    else:
        return render(request,"Govt_Add_Farmer.html")

def Govt_Up_Farmer(request):
    uid = request.GET["id"]
    res = Govt.objects.filter(id=uid)
    return render(request,"Govt_Update_Farmer.html",{"r":res})

def Govt_Update_Farmer(request):
    Id = request.POST["Uid"]
    First_Name = request.POST['ufname']
    Last_Name = request.POST['ulname']
    House_Number = request.POST['uhouseno']
    Village_Name = request.POST['uvillage']
    Mandal_Name = request.POST['umandal']
    District_Name = request.POST['udistrict']
    State_Name = request.POST['ustate']
    Aadhaar_Number = request.POST['uaadhaar']
    PassBook_Number = request.POST['upassbook']
    Land = request.POST['uland']

    Govt.objects.filter(id = Id).update(First_Name=First_Name,Last_Name=Last_Name,House_Number=House_Number,
                        Village_Name=Village_Name,Mandal_Name=Mandal_Name,District_Name=District_Name,
                        State_Name=State_Name,Aadhaar_Number=Aadhaar_Number,PassBook_Number=PassBook_Number,
                        Land=Land)

    return redirect("gdata")

def Govt_Delete_Farmer(request):
    Did = request.GET["id"]
    Govt.objects.filter(id=Did).delete()
    return redirect("gdata")

def Admin_Up_Seller(request):
    id = request.POST["id"]
    res = Seller.objects.filter(id=id)
    return render(request,"Admin_Update_Seller.html",{"r":res})

def Admin_Update_Seller(request):
    Uid = request.POST['id']
    Full_Name = request.POST['UName']
    Email_Id = request.POST['UEmail']
    Mobile_No = request.POST['UMobile']
    Shop_Name = request.POST['UShopName']
    Shop_Id = request.POST['UShopId']
    Address = request.POST['UAddress']

    Seller.objects.filter(id=Uid).update(Full_Name=Full_Name,Email_Id=Email_Id,Mobile_No=Mobile_No,
                        Shop_Name=Shop_Name,Shop_Id=Shop_Id,Address=Address)
    return redirect("ddata")

def Admin_Delete_Seller(request):
    Did = request.GET["id"]
    Seller.objects.filter(id=Did).delete()
    return redirect("ddata")

def Admin_Delete_Farmer(request):
    Did = request.GET["id"]
    Customer.objects.filter(id=Did).delete()
    return redirect("fdata")
