from django.shortcuts import render

# Create your views here.

def jugar(request):
    return render(request,"jugar/juego.html",{"Nombre":"nombre"})
