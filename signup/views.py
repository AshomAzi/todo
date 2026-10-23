from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def signup(request):

    if request.method == "POST":
        first_name = request.POST["firstname"].strip().capitalize()
        last_name = request.POST["lastname"].strip().capitalize()
        username = request.POST["username"].strip().lower()
        email = request.POST["email"].strip()
        password1 = request.POST["password1"]
        password2 = request.POST["confirmPassword"]


        if password1 != password2:
            messages.error(request, "Password does not match")
            return redirect("signup")

        if len(password1) < 8:
            messages.error(request, "Password Must be 8 Characters long")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken, try to login!")
            return redirect(request, "signup")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username has beed taken.")
            return redirect("signup")
        

        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            email=email,
            username=username,
            password=password1
        )

        user.save()
        return redirect("signin")
    else:
        return render(request, "signup.html")