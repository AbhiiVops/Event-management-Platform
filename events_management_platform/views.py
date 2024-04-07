from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from events.models import EventCategory, Event
from .forms import LoginForm
from django.http import HttpResponse

@login_required(login_url='login')
def dashboard(request):
    user = User.objects.count()
    event_ctg = EventCategory.objects.count()
    event = Event.objects.count()
    complete_event = Event.objects.filter(status='completed').count()
    events = Event.objects.all()
    context = {
        'user': user,
        'event_ctg': event_ctg,
        'event': event,
        'complete_event': complete_event,
        'events': events
    }
    return render(request, 'dashboard.html', context)

def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return HttpResponse('Username or Password is incorrect')
    context = {
        'form': forms
    }
    return render(request, 'login.html', context)


def RegisterPage(request):
    if request.method == 'POST':
         uname= request.POST.get('username')
         email= request.POST.get('email')
         pass1= request.POST.get('password1')
         pass2= request.POST.get('password2')

         if pass1 != pass2:
             return HttpResponse('Password Are Not Matching')
         else :

             my_user= User.objects.create_user(uname, email, pass1)
             my_user.save()
         
        # return HttpResponse('User Created Successfully')
         
         return redirect('login')
    
    return render(request, 'register.html')

def forgot_page(request):
    if request.method == 'POST':
        # Process form submission here (e.g., send password reset email)
        pass
    return render(request, 'forgot-password.html')

def logut_page(request):
    logout(request)
    return redirect('login')