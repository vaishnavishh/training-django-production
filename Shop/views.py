from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Contact



def index(r):
    if not request.user
    return render(r, 'index.html')

def products(r):
    return render(r, 'products.html')

def about(r):
    return render(r, 'about.html')

def contact(r):
    if r.method == "POST":
        n = r.POST.get('name')
        p = r.POST.get('phone')
        e = r.POST.get('email')
        m = r.POST.get('msg')
        o = Contact(name=n, phone=p, emailid=e, msg=m)
        o.save()
        return redirect('/contact/')
    d = Contact.objects.all()
    return render(r, 'contact.html', {'data': d})

def catalogue(r):
    return render(r, 'catalogue.html')

def signupView(r):
    if r.method == "POST":
        m5 = r.POST.get('emailAddress')
        m6 = r.POST.get('username')
        m7 = r.POST.get('password')
        cpassword = r.POST.get('cpassword')
        firstName = r.POST.get('firstName')
        lastName = r.POST.get('lastName')

        if m7 == cpassword:
            user = User.objects.create_user(username=m6, email=m5, password=m7)
            user.first_name = firstName
            user.last_name = lastName
            user.save()
            return redirect('/signup/')
            
    return render(r, 'signup.html')

def loginView(r):
    if r.method == "POST":
        user = authenticate(username="john", password="secret")
        if user is not None:
            # A backend authenticated the credentials
            pass
        else:
            # No backend authenticated the credentials
            pass

    return render(r, 'login.html')

def logoutView(request):
    logout(request)
    return redirect(('/login'))
