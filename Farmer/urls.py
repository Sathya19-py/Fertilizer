from django.urls import path
from Farmer import views

urlpatterns = [
    path("",views.Home,name="home"),
    path("product",views.ProductHome,name="product"),
    path('registration', views.Registration, name="registration"),
    path('customer_login', views.CustLogin, name="customer_login"),
    path('contact',views.Contact,name="contact"),
    path('track',views.Track,name="track"),
    path('fhome',views.Farmer_Home,name='fhome'),
    path('fproduct',views.Farmer_Product,name='fproduct'),
    path("addcart",views.AddCart,name="addcart"),
    path("deletecart",views.DeleteCart,name="deletecart"),
    path("single",views.Single,name="single"),
    path("check",views.CheckOut,name="check"),
    path('fcart',views.Farmer_Cart,name='fcart'),
    path('adquanty',views.Add_Delete,name='adquanty'),
    path('forders',views.Farmer_Orders,name='forders'),
    path('details',views.Order_Details,name='details'),
    path('fnotifications',views.Farmer_Notifications,name='fnotifications'),
    path('ftrack',views.Farmer_Track,name='ftrack'),
    path('ftracking',views.Tracking,name='ftracking'),
    path('finfo',views.Farmer_Info,name='finfo'),
    path('faddress',views.FAddress,name="faddress"),
    path('newaddress',views.AddAddress,name="newaddress"),

]
