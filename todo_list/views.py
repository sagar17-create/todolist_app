from django.shortcuts import render, redirect
from .models import Textbox
from user.views import auth, login
from django.contrib.auth.decorators import login_required
# import re


def delete(request, number):
    Textbox.objects.get(id=number).delete()
    return render(request, 'home.html', {"dicts": Textbox.objects.all()})


@login_required(login_url="/home")
def index(request):
    if request.method == "POST":
        data = request.POST["search"]
        print(data)
        Textbox.objects.create(name=data.title())
        return render(request, 'home.html', {"dicts": Textbox.objects.all()})
    else:
        return render(request, 'home.html', {"dicts": Textbox.objects.all()})


def update(request, id):
    if request.method == "POST":
        textbox = Textbox.objects.filter(pk=id)
        textbox.update(name=request.POST["name"].title())

    return render(request, 'home.html', {"dicts": Textbox.objects.all()})


def search(request):
    if request.method == "POST":
        searched = request.POST["search"].title()
        print(searched)
        return render(request, 'searched_list.html', {'dicts': Textbox.objects.filter(name__startswith=searched)})

    else:
        return render(request, "searched_list.html")
