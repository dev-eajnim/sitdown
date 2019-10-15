from django.shortcuts import render
import hello

# Create your views here.
def home(request): #메인화면 열기 
    return render(request, 'main.html')

def seat(request): 
    return render(request, 'seat.html')

def sub(request):
    return render(request, 'sub.html')


