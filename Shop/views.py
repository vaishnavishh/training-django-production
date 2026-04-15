from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Contact

def index(request):
    # Simplified: Renders index.html for everyone. 
    # Handle the user-specific display inside the HTML using {% if user.is_authenticated %}
    return render(request, 'index.html') 

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        n = request.POST.get('name')
        p = request.POST.get('phone')
        e = request.POST.get('email')
        m = request.POST.get('msg')
        
        o = Contact(name=n, phone=p, emailid=e, msg=m)
        o.save()
        
        # Best practice: use the URL name defined in your urls.py (assuming it is named 'contact')
        return redirect('contact')
        
    d = Contact.objects.all()
    return render(request, 'contact.html', {'data': d})

def catalogue(request):
    return render(request, 'catalogue.html')

def signupView(request):
    if request.method == "POST":
        m5 = request.POST.get('emailAddress')
        m6 = request.POST.get('username')
        m7 = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')

        # Check to ensure core fields aren't accidentally submitted blank
        if not all([m5, m6, m7]):
            return render(request, 'signup.html', {'error': 'Username, email, and password are required.'})

        if m7 == cpassword:
            # Prevent crashes if two users try to register the same name
            if User.objects.filter(username=m6).exists():
                return render(request, 'signup.html', {'error': 'Username is already taken.'})
            
            user = User.objects.create_user(username=m6, email=m5, password=m7)
            user.first_name = firstName
            user.last_name = lastName
            user.save()
            return redirect('login') 
        else:
            # Added an error in case passwords don't match
            return render(request, 'signup.html', {'error': 'Passwords do not match.'})
            
    return render(request, 'signup.html')

def loginView(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        user = authenticate(request, username=u, password=p)
        
        if user is not None:
            login(request, user)
            return redirect('index') # Redirect to home page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials.'})

    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('login')