from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import User,Address
from django.contrib import messages
# from django.core.exceptions import AttributeError

# Create your views here.
def signup(request):
    if request.method=='POST':
        profile_picture=request.FILES.get('profile_picture')
        first_name=request.POST['firstName']
        last_name=request.POST['lastName']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirmPassword']
        role=request.POST['userType']
        street=request.POST['streetAddress']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']
        country=request.POST['country']
        user=User.objects.create_user(profile_picture=profile_picture,first_name=first_name,last_name=last_name,username=username,email=email,password=password,role=role)
        Address.objects.create(user=user,street=street,city=city,state=state,pincode=pincode,country=country)
        return redirect('/login')

    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/dashboard')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/login')
        
    return render(request,'login.html')


def dashboard(request):
    try:     
        user=request.user
        # print(user)
        address=user.address
        return render(request,'dashboard.html',{'user':user,'address': address})

    except AttributeError:
        messages.error(request,'you must login to view dashboard')
        return redirect('/login')




def signout(request):
    logout(request)
    return redirect('/login')