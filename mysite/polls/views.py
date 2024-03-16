from django.shortcuts import render
from datetime import datetime
from polls.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def housing(request):
    return render(request,'housing.html')

def commercial(request):
    return render(request,'commercial.html')

def upload(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        link = request.FILES.get('link')
        
        contact = Contact(email = email, password = password, phone = phone, address = address, city = city, state = state, zipcode = zipcode, profile_picture = link, date = datetime.today())
        try:
            contact.save()
            messages.success(request,'Property details uploaded')
        except:
           messages.error(request,"You should check in some of the fields below") 
        
    return render(request,'upload.html')

def contact(request):
    # if post request aarahi hai tau database mei store kardo
    return render(request,'contact.html')

