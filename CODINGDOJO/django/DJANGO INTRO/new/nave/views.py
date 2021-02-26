from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime
    
def index(request):
    context = {
        "time": strftime("%b %d, %Y", localtime()),
        "hora":strftime("%H:%M %p",localtime())
    }
    return render(request,'first.html', context)

def prueba(request):
    nombre="Camila"
    apellido="riquelme"
    context= {"nombre_persona":nombre,"apellido":apellido}

    return render(request,'prueba.html',context)

def padre(request):
    context = {
        "time": strftime("%b %d, %Y", localtime()),
        "hora":strftime("%H:%M %p",localtime())
    }
    return render(request, 'hija.html',context)