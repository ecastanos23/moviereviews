from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    #return HttpResponse('<h1>Welcome to the Movie Reviews Home Page</h1>')
    return render(request, 'home.htm', {'name': 'Chun-Li'})

def about(request):
    return HttpResponse('<h1>Esta es la página About</h1>')