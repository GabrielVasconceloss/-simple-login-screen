from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class Home(TemplateView):
    template_name = 'home.html'


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
            return HttpResponse('Ja existe um User com esse nome')

        user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                        email=email, password=password)
        user.save()

        return HttpResponse(f'Usuario {username} Cadastrado com susseso ')


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
            return HttpResponse('Não ache man ' + str(user))


@login_required(login_url='auth/login/')
def platform(request):
    return render(request, 'login.html')
