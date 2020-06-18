from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home/")
        elif auth.authenticate(username=username) is not None and auth.authenticate(password=password) is None:
            messages.info(request, "incorrect password")
            return render(request, "error_msg.html")
        else:
            messages.info(request, "invalid User")
            return render(request, "error_msg.html")




    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        name = request.POST["username"]
        mail = request.POST["mail"]
        password = request.POST["password"]
        password1 = request.POST["password1"]
        if password == password1:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'Username Already Exist')
                return render(request, "error_msg.html")
            elif User.objects.filter(email=mail).exists():
                messages.info(request, "Email Already Exist")
                return render(request, "error_msg.html")
            else:
                user = User.objects.create_user(username=name, email=mail, password=password)
                user.save()
                return redirect("/")
        else:
            messages.info(request, "Password Did't Match")
            return render(request, "error_msg.html")
    else:
        return render(request, 'signup.html')
