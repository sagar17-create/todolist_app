from django.shortcuts import render, redirect
from .models import Textbox


def delete(request, number):
    Textbox.objects.get(id=number).delete()
    return render(request, 'home.html', {"dicts": Textbox.objects.all()})


def index(request):
    if request.method == "POST":
        data = request.POST["search"]
        Textbox.objects.create(name=data.title())
        return render(request, 'home.html', {"dicts": Textbox.objects.all()})
    else:
        return render(request, 'home.html', {"dicts": Textbox.objects.all()})


def update(request, id):
    if request.method == "POST":
        textbox = Textbox.objects.filter(pk=id)
        textbox.update(name=request.POST["name"].title())

    return redirect("home/")
