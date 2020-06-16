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
        data = request.POST["search"]
        textbox = Textbox(name = request.POST["name"])
        Textbox.objects.get(pk = id).update(Textbox = textbox)
        
        return "success"
            
     

    return render(request,'update.html')


