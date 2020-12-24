from django.urls import path
from Admin import views

urlpatterns = [
    path("",views.Admin_Login,name="alogin"),
    path("fdata",views.Farmer_Data,name="fdata"),
    path("ddata",views.Dealer_Data,name="ddata"),
    path("gdata",views.Govt_Data,name="gdata"),
    path("govtaddfarmer",views.Govt_Add_Farmer,name="govtaddfarmer"),
    path("govtupfarmer",views.Govt_Up_Farmer,name="govtupfarmer"),
    path("govtupdatefarmer",views.Govt_Update_Farmer,name="govtupdatefarmer"),
    path("govtdeletefarmer",views.Govt_Delete_Farmer,name="govtdeletefarmer"),
    path("adminupseller",views.Admin_Up_Seller,name="adminupseller"),
    path("adminupdateseller",views.Admin_Update_Seller,name="adminupdateseller"),
    path("admindeleteseller",views.Admin_Delete_Seller,name="admindeleteseller"),
    path("adminfarmerdelete",views.Admin_Delete_Farmer,name="adminfarmerdelete"),
]
