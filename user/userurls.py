from django.contrib import admin
from django.urls import path
from . import views
urlpatterns =[
     path('',views.index,name='index'),
     path('ride',views.ride,name="ride"),
     path('registration',views.registration,name='registration'),
     path('signin',views.signin,name='signin'),
     path('logout/', views.logout_view, name='logout'),
     path('login',views.login,name='login'),
     path('contact',views.contact,name='contact'),
     path('logcode',views.logcode,name="logcode"),
     path('service', views.service, name='service'),
     path('support', views.support, name = 'support'),
     path('success', views.success, name = 'success'),
     path('book/<int:id>/', views.book_vehicle, name='book_vehicle'),
     path('inquiry-form/', views.inquiry_form_view, name='inquiry_form'),
     path('booking/', views.booking_view, name='booking_view'),
    path("booking/success/<str:booking_id>/<str:pickup_date>/<str:dropoff_date>/",views.booking_success, name="booking_success"),
     
     path('about', views.about, name='about_us'),

    
]

