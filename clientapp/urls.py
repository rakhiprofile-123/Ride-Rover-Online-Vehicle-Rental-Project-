from django.urls import path
from .import views

urlpatterns=[
   path('clientapp/',views.clientdash,name="clientdash"),
   path('clientlogout/',views.clientlogout,name="clientlogout"),
]