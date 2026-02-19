from django.shortcuts import render,redirect,reverse, get_object_or_404
from .models import LoginUser
from .models import Registration
from .models import Vehicle
from .models import BookVehicle
from .models import Inquiry
from .models import Booking 
from adminapp.forms import BookingForm
from django.utils import timezone


from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now 

import json

def index(request):
    return render(request,'index.html')

def ride(request):
    return render(request,'ride.html')

def registration(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        emailid = request.POST['emailid']
        password = request.POST['password'] 
        mob_number = request.POST['mob_number']
        licensenumber = request.POST['licensenumber']
        licensepic = request.FILES['licensepic']
        signpic = request.FILES['signpic']

        
        if Registration.objects.filter(emailid=emailid).exists():
            messages.error(request, "Email already registered.")
            return redirect('signin')

        
        user = Registration(
            fullname=fullname,
            emailid=emailid,
            password=password,
            mob_number=mob_number,
            licensenumber=licensenumber,
            licensepic=licensepic,
            signpic=signpic
        )
        user.save()
        # messages.success(request, "Registration successful! Please log in.")
        return redirect('signin')
    return render(request, 'registration.html')
   

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('emailid')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password!")
            return render(request, 'signin.html')  
        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            login(request)
            # messages.success(request, f"Welcome back, {user.username}!")
            return redirect('index')
        else:
            messages.error(request, "Invalid email or password!")
            return render(request, 'signin.html')  

    return render(request, 'signin.html') 

def logout_view(request):
    logout(request)
    return redirect('index')
       


def login(request):
    return render(request,'login.html')

def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request, 'service.html')

def support(request):
    return render(request, 'support.html')

def success(request):
    return render(request, 'success.html')

def logcode(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        usertype = request.POST.get('usertype', '').strip()

        try:
            user = LoginUser.objects.get(username=username, password=password, usertype=usertype)

            if user.usertype.lower() == "admin":
                request.session['username'] = username
                return redirect('adminapp:dash')
            elif user.usertype.lower() == "user":
                request.session['username'] = username
                return redirect('clientapp:clientdash')
        except LoginUser.DoesNotExist:
           
            print(f"No user found with username={username}, password={password}, usertype={usertype}")
            return redirect('signin')
    else:
        
        return redirect('ride')
        

def service(request):
    vehicles = Vehicle.objects.all()  
    return render(request, 'service.html', {'vehicles': vehicles})




# from admin.forms import BookingForm  # Assuming you have created a BookingForm as discussed earlier


    # Get the specific vehicle by its ID
    

   
    # if request.method == 'POST':
    #     form = BookingForm(request.POST)
    #     if form.is_valid():
    #         booking = form.save(commit=False)
    #         booking.vehicle = book_vehicle 
    #         booking.save()
    #         return redirect('booking_success')  

    # else:
    #     form = BookingForm()

    
    
@login_required
def book_vehicle(request, id):
    vehicle = get_object_or_404(BookVehicle, id=id)
    
    return render(request, 'book_vehicle.html', {'vehicle': vehicle})

def inquiry_form_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
 
        Inquiry.objects.create(
            name=name,
            mobile=mobile,
            email=email,
            subject=subject,
            message=message,
        )

        messages.success(request, "Your inquiry has been submitted successfully!")
        return redirect('index')  

    return render(request, 'index.html')



@login_required
def booking_view(request):
    if request.method == "POST":
        # vehicle = Vehicle.objects.get(id=vehicle_id)
        booking_type = request.POST.get("booking_type")
        pickup_date = request.POST.get("pickup_date")
        pickup_time = request.POST.get("pickup_time")
        dropoff_date = request.POST.get("dropoff_date")
        dropoff_time = request.POST.get("dropoff_time")
        # duration = (dropoff_date_obj - pickup_date_obj).days
        
        
        # if booking_type == 'daily':
        #     base_rate = vehicle.price_per_day * duration
        # elif booking_type == 'weekly':
        #     base_rate = vehicle.price_per_week * (duration // 7) 
        # else:  
        #     base_rate = vehicle.price_per_month * (duration // 30)  
        # taxes = base_rate * 0.18
        # total_amount = base_rate + taxes

        
       
        booking = Booking.objects.create(
            # vehicle=vehicle,
            user = request.user,
            booking_type=booking_type,
            pickup_date=pickup_date,
            pickup_time=pickup_time,
            dropoff_date=dropoff_date,
            dropoff_time=dropoff_time,
            
            
        )

        return redirect("booking_success", booking_id=booking.booking_id, pickup_date=pickup_date, dropoff_date=dropoff_date )

    return render(request, "book_vehicle.html")

def booking_success(request, booking_id, pickup_date, dropoff_date):
    return render(request, "booking_success.html", {
        "booking_id": booking_id,
        "pickup_date": pickup_date,
        "dropoff_date": dropoff_date
    })

def about(request):
    return render(request,'about_us.html')


