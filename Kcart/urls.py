from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = "KcartHome"),
    path('login/',views.Login,name = "Login"),
    path('register/',views.Register,name = "Register"),
    path('about/',views.About,name = "About"),
    path('contact/',views.contact,name = "ContactUs"),
    path('search/',views.Search,name = "Search"),
    path('cart/',views.Cart,name = "Cart"),
    path('checkout/',views.CheckOut,name = "CheckOut"),
    path('success/',views.Success,name = "success"),
    path('productView/<int:myid>',views.ProductView,name = "ProductView"),
    path('tracker/',views.Tracker,name = "tracker"),
]