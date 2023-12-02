from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def index_view(request):
    return render(request, 'index.html')


@login_required
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).filter()
        if user:
            messages.info(request, 'Username already registered!', extra_tags='danger')
            return render(request, 'register.html')

        if password.lower() == password:
            messages.info(request, 'Password must contain an uppercase!', extra_tags='danger')
            return render(request, 'register.html')
        else:
            user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                            email=email, password=password)
            user.save()
            messages.info(request, 'User created successfully!', extra_tags='success')
            return render(request, 'login.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return render(request, 'home.html')
        else:
            messages.info(request, 'User not found!', extra_tags='danger')
            return render(request, 'login.html')


def logout_(request):
    logout(request)
    return render(request, 'login.html')