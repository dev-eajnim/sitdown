from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import accounts

# Create your views here.
def signup(request): #home(회원가입페이지로 이동) 회원가입 처리 # 되면 핸드폰번호 , 이름 까지 수정 
    return render(request, 'home.html')

# def accounts(request):
    # return render(request, 'home.html')

