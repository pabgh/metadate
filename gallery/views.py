from django.shortcuts import render

def index(request):
    return render(request, 'gallery/index.html')

def login(request):
    return render(login, 'gallery/login.html')