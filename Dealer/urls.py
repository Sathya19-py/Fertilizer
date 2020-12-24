from django.urls import path
from . import views

urlpatterns = [
    path('',views.SellLogin,name="seller_login"),
    path('sell_with',views.SellWithUs,name="sell_with"),
    path('dhome',views.Home,name="dhome"),
    path("add",views.Add_Product,name="add"),
    path("delete_and_update",views.Delete_Update,name="delete_and_update"),
    path('dorders',views.Orders,name='dorders'),
    path("deliverystatus",views.Delivery_Status,name="deliverystatus"),
    path("delete",views.Delete,name="delete"),
    path("update",views.Update,name="update"),
    path("updatep",views.Update_Product,name="updatep"),
]

