from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('custumer/<str:hqq>', views.custumer, name='custumer'),
    path('create_order/', views.createOrder, name='create_order'),
    path('create_custumer/', views.createcustumer, name='create_custumer'),
    path('update_order/<str:lpp>', views.updateOrder, name='update_order'),
    path('delete_order/<str:anj>', views.deleteOrder, name='delete_order'),
    path('delete_custumer/<str:apb>', views.deleteCustumer, name='delete_custumer'),
    path('update_custumer/<str:apa>', views.updateCustumer, name='update_custumer'),
  
]