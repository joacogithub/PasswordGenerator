from django.shortcuts import render
import random 

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):
    
    characters = list('abcdefghijklmnñopqrstuvwxyz')
    
    length = int(request.GET.get('length'))
    generated_password = ''
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    
    for x in range(length):
        
        generated_password += random.choice(characters)
    
    return render(request, 'password.html', {
        'password': generated_password
    })