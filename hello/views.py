from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main.html')

def create(request):
    return render(request, 'home.html')

def seat(request):
    return render(request, 'seat.html')

def sub(request):
    return render(request, 'sub.html')
