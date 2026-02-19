from django.contrib import admin
from django.urls import path,include
from . import views
from .views import*


urlpatterns=[
    path('dash',views.index,name="dash"),
    path('register/', views.register, name='register'),
    path('custmng/', views.custmng, name='custmng'),
    path('logout',logout,name="logout"),
    path('delcust/<id>',views.delcust,name="delcust"),
    path('provider',views.provider,name="provider"),
    path('delprovider/<id>',views.delprovider,name="delprovider"),
    path('admin_inquiries', views.inquiry_admin_view, name="inquiries"),
    path('vehicle', views.vehicle, name = "vehicle"),
    path('delvehicle/<id>',views.delvehicle,name="delvehicle"),
    path('bookings_details', views.booking_details, name = 'bookings_details'),
    path('logout',views.logout,name="logout"),
   
    
    
]