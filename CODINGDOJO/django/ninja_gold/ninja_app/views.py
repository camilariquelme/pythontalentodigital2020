from django.shortcuts import render, HttpResponse
from random import randint, uniform,random
from time import gmtime, strftime, localtime


def index(request):
    request.session['log']=[]
    request.session['gold']=0
    return render (request, 'index.html')
def process_money(request):
    #print (request.POST["opcion"]) ---se puede verificar que el boton recibe informacion
    gold=request.session['gold']
    log=request.session['log']
    text=""
    class2="style=color:green"
    num=0
    if request.POST["opcion"]=="farm":
        num=randint(10,20)
        text=f"earned {num} golds from farm" 
        
    elif request.POST["opcion"]=="cave":
        num=randint(5,10)
        text=f"earned {num} golds from cave "

    elif request.POST["opcion"]=="house":
        num=randint(2,5)
        text=f"earned {num} golds from house "


    elif request.POST["opcion"]=="casino":
        num=randint(-50,50)
        if num >=0 :
            text=f"earned {num} golds from casino "

        else:
            class2="style=color:red"
            text=f"entered a casino and lost {num} golds ...ouch "

    gold=gold+num
    text2={
            "mensaje":text,
            "time": strftime("%Y %b %d, %H:%M %p", localtime()),
            "class":class2
            
        }
    log.append(text2)

    request.session['gold']=gold
    request.session['num']=num
    return render (request, 'index.html')
