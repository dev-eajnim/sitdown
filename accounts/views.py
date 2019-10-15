from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import accounts
import hello

# Create your views here.
def signup(request): #home(회원가입페이지로 이동)
    if request.method == 'POST':
        user = User.objects.create_user(
            request.POST['username'], password=request.POST['password'])
        auth.login(request, user)
        return redirect('main')
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'main.html', {'error': 'ID or password is incorrect.'})
    else:
        return render(request, 'main.html', {'oo': 'ID or password is incorrect.'} )

