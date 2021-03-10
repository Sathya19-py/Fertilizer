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

    path('insertproduct/',views.ProductOperations.as_view({"post":"create","get":"list",})),
    # path('viewproduct/',views.ProductOperations.as_view({"get":"list"})),
    path('updateproduct/<int:pk>',views.ProductOperations.as_view({"put":"update"})),
    path('deleteproduct/<int:pk>',views.ProductOperations.as_view({"delete":"destroy"})),
    path('partialproduct/<int:pk>',views.ProductOperations.as_view({"patch":"partialupdate"})),

    path('readproducts/',views.ReadProducts.as_view({'get': 'list'})),
    path('readproduct/<int:pk>',views.ReadProducts.as_view({'get': 'retrieve'})),

]

