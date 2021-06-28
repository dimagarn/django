from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from user_profile.forms import UserForm
from user_profile.models import MainCycle


def index(request):
    user = User.objects.filter(id=request.user.id)
    if len(user) != 0:
        mainCycle = MainCycle.objects.filter(user=request.user)[0]
        return render(request, 'index.html', {'user':user[0], 'mainCycle':mainCycle})
    else:
        return redirect('login')

def user_login(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'invalid':True})
    else:
        return render(request, 'login.html', {'invalid':False})


def user_logout(request):
    logout(request)
    return redirect('login')


def user_registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            mainCycle = MainCycle()
            mainCycle.user = user
            mainCycle.save()
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return redirect('index')

        else:
            return render(request, 'registration.html', {'invalid':True, 'form': form})
    else:
        form = UserForm()
        return render(request, 'registration.html', {'invalid':False, 'form': form})
