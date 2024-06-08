from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def registration(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        mobile = request.POST['mobile']
        user = User.objects.create_user(username=email, first_name=fname, last_name=lname, email=email, password=password)
        UserProfile.objects.create(user=user, mobile=mobile, address=address)
        messages.success(request, "Registeration Successful")
    return render(request, 'registration.html', locals())


def userlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "User login successfully")
            return redirect('Hospital_list')
        else:
            messages.success(request,"Invalid Credentials")
    return render(request, 'userlogin.html', locals())
def Hospital_list(request):
    if request.method == 'POST':
        # Retrieve selected course and subject IDs from the form submission
        hospital_id = request.POST.get('hospital')
        phoneNo = request.POST.get('phoneNo')
        # Fetch related questions based on course and subject
        patients = Patient.objects.filter(hospital_id=hospital_id,phoneNo=phoneNo)
        # Render the template with the fetched questions
        return render(request, 'hospital_list.html', {'patients': patients})

    # If the request method is GET, render an empty form
    hospitals = Hospital.objects.all()
    patient = Patient.objects.all()
    return render(request, 'hospital_form.html', {'hospitals':hospitals , 'patient': patient})

def report(request, Patient_id):
    patient = get_object_or_404(Patient, id=Patient_id)
    reports = Report.objects.filter(patient=patient)
    return render(request, 'report.html', {'patient': patient, 'reports': reports})