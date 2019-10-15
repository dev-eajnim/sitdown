from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import hello
import accounts

# Create your views here.
# def home(request): #메인화면 열기 
#     return render(request, 'main.html')

def seat(request): 
    return render(request, 'seat.html')

def sub(request):
    return render(request, 'sub.html')

def login(request):
    if request.method == 'POST':
        ID = request.POST['ID']
        password = request.POST['password']
        user = auth.authenticate(request, ID=ID, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'main.html', {'error': 'ID or password is incorrect.'})
    else:
        return render(request, 'main.html')

def signup(request): #home(회원가입페이지로 이동)
    if request.method == 'POST':
        user = User.objects.create_user(
            request.POST['ID'], password=request.POST['password'])
        auth.login(request, user)
        return redirect('main')
    return render(request, 'home.html')


