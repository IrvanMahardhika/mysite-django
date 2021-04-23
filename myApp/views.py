# 'redirect' below is added
from django.shortcuts import render, redirect

# Create your views here.

# added
from .forms import RegisterForm

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home") 
    else:
        form = RegisterForm()
    
    return render(response, "myApp/register.html", {"form": form})
    