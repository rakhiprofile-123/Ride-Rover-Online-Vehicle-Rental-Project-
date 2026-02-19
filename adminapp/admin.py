from django.contrib import admin
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
from user.models import *

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'emailid', 'password', 'mob_number', 'licensenumber', 'licensepic')
    list_filter = ('date_registered',)
    search_fields = ('fullname', 'emailid', 'licensenumber', 'mob_number')


class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'subject', 'message', 'submitted_at')
    search_fields = ('name', 'email', 'mobile', 'subject')
    list_filter = ('submitted_at',)
    ordering = ('-submitted_at',)

class VehicleAdmin(admin.ModelAdmin): 
    list_display = ('name', 'price_per_day', 'security_deposit', 'image')  
    search_fields = ('name')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'booking_type', 'pickup_date', 'dropoff_date', 'total_amount')
    list_filter = ('booking_type', 'pickup_date', 'dropoff_date')  
    search_fields = ('user__username', 'name')

    def get_queryset(self, request):
       
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  
        return qs.filter(user=request.user) 



