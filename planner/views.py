from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages
from django.contrib.sessions.models import  Session
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
# Create your views here.
def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username,email=email,password=password)

        request.session['signup_username'] = username
        request.session['signup_email'] = email
        request.session['signup_password'] = password

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Successfulyy signed up!')
            return redirect('login')

    return render(request,template_name='signup.html')




def login(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Successfulyy Logged In!')
            return redirect('home')
    return render(request,template_name='login.html')

@login_required
def home(request):

    user = request.user
    context = {
        'user' : user

    }

    return render(request,template_name='home.html',context=context)

# def plantrip(request):
#     return render(request,template_name='journeyform.html')




def add_plan(request):
    form = PlantripForm()
    if request.method == 'POST':
        form = PlantripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={
        'form':form,
    }
    return render(request,template_name='plantrip.html', context=context)




# views.py


def create_plantrip(request):
    if request.method == 'POST':
        form = PlantripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = PlantripForm()
    return render(request, 'plantrip.html', {'form': form})




def plantrip(request):
    if request.method == 'POST':
        departure = request.POST.get('departure')
        destination = request.POST.get('destination')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        starttime = request.POST.get('starttime')
        endtime = request.POST.get('endtime')
        grouptrip = request.POST.get('grouptrip')
        solotrip = request.POST.get('solotrip')

        # Convert grouptrip and solotrip strings to boolean values
        grouptrip = True if grouptrip == 'on' else False
        solotrip = True if solotrip == 'on' else False

        # Create Plantrip object
        plan = Plantrip(
            departure=departure,
            destination=destination,
            startdate=startdate,
            enddate=enddate,
            starttime=starttime,
            endtime=endtime,
            grouptrip=grouptrip,
            solotrip=solotrip
        )
        # Save the Plantrip object to the database
        plan.save()

        # Optionally, you can add a success message
        messages.success(request, 'home')

        # Redirect to a success page or any other appropriate page
        return redirect('home')  # Change 'success_page' to the name of your success page URL pattern
    
    # Render the form template for GET requests
    return render(request, 'journeyform.html')  # Change 'plantrip_form.html' to the name of your HTML template



def tourguide(request):
    tourguide=Tourguide.objects.all()
    context= {
        'tourguide': tourguide,
    }

    return render(request,template_name='tourguide.html', context=context )\



def guide_details(request, id):
    buy = Tourguide.objects.get(pk = id)
    context ={
        'buy': buy,
    }
    return render(request,template_name='guide_details.html',context=context)


def logout_user(request):
     logout(request)
     messages.success(request,'Youre logged out!')
     return redirect('signup')



