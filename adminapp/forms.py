from django import forms
from user.models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['fullname', 'emailid', 'mob_number', 'licensenumber', 'licensepic', 'userpic', 'signpic']
        widgets = {
            'licensepic': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'userpic': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'signpic': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['booking_type', 'pickup_date', 'pickup_time', 'dropoff_date', 'dropoff_time']
#         widgets = {
#             'pickup_date': forms.DateInput(attrs={'type': 'date'}),
#             'dropoff_date': forms.DateInput(attrs={'type': 'date'}),
#             'pickup_time': forms.TimeInput(attrs={'type': 'time'}),
#             'dropoff_time': forms.TimeInput(attrs={'type': 'time'}),
#         }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_type', 'pickup_date', 'pickup_time', 'dropoff_date', 'dropoff_time']
        widgets = {
            'pickup_date': forms.DateInput(attrs={'type': 'date'}),
            'pickup_time': forms.TimeInput(attrs={'type': 'time'}),
            'dropoff_date': forms.DateInput(attrs={'type': 'date'}),
            'dropoff_time': forms.TimeInput(attrs={'type': 'time'}),
        }
