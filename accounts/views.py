from django.shortcuts import render
from .forms import UserRegisterForm
from accounts.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# REGISTER OWNERS OF THE COMPANY
def register_admin(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            role = 'Administrator'  
            group, created = Group.objects.get_or_create(name=role)
            # user = User.objects._create_user(username=username, email=email, password=password)
            user = User.objects.create(username=username, email=email, password=password)
            user.groups.add(group)
            messages.success(request, 'You have successfully registered as an owner.')
            return redirect('profile')
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

def register_jobseeker(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            password = form.cleaned_data['password2']
            email = form.cleaned_data['email']

            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()

            roles = request.GET.get('role', 'Jobseeker')
            
            group_name = 'Jobseeker'
            group, created = Group.objects.get_or_create(name=group_name)

            user.groups.add(group)
            messages.success(request, 'You have successfully registered as a jobseeker.')
            return redirect('home')
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/jobseeker.html', context)


def profile(request):
    return render(request, 'accounts/profile.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfull')
            return redirect('home')
        else:
            messages.success(request, 'There was an error login in')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')

def password_reset(request):
    return render(request, 'accounts/password_reset_form.html', {})