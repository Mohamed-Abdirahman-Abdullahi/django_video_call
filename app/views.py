from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'lobby.html')

def room(request):
    return render(request, 'room.html')