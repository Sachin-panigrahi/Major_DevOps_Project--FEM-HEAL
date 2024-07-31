from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import views as auth_views
from django.conf import settings

from .models import Doctor
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,"index.html")


def imprint(request):
    return render(request,"Impressum.html")

@login_required
def health(request):
    return render(request,"health.html")

def login(request):
    return render(request,"login.html")



# views.py

from django.http import JsonResponse
from .models import Doctor

from django.shortcuts import render
from .models import Doctor
import requests



# @login_required
def customer_reviews(request):
    return render(request,"customer_reviews.html")
@login_required
def health_issue(request):
    return render(request,"health_issues.html")
@login_required
def physical_health(request):
    return render(request,"physical_health.html")

@login_required
def mental_health(request):
    return render(request,"mental_health.html")
@login_required
def menstrual_health(request):
    return render(request,"menstrual_health.html")



# views.py
# from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Doctor
@login_required
def doctor_list(request):
    query = request.GET.get('q')  # Get the search query from the URL parameters
    if query:
        # Filter doctors by name or specialty, case-insensitive
        doctors = Doctor.objects.filter(name__icontains=query) | Doctor.objects.filter(speciality__icontains=query)
    else:
        doctors = Doctor.objects.all()  # If no query, get all doctors

    return render(request, 'doctor_list.html', {'doctors': doctors})

@login_required
def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, 'doctor_detail.html', {'doctor': doctor})
@login_required
def doctor_location(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, 'doctor_location.html', {'doctor': doctor})


class CustomLoginView(auth_views.LoginView):
    def get_success_url(self):
        return redirect('')
    

from django.contrib.auth import logout
from django.views import View   
class CustomLogoutView(View):
 def get(self, request):
    logout(request)
    return redirect('/') 
    


# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            # If the form is not valid, show errors
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})
