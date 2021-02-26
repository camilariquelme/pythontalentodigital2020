from django.shortcuts  import render, HttpResponse
from django.utils.crypto import get_random_string
def index(request):
    request.session['counter'] = 0
    return render (request, 'index.html')
def random_word(request):
    request.session['counter']+=1
    context={
        "letras":get_random_string()
    }
    return render(request, "index.html",context)
def reset(request):
    request.session['counter'] = 0
    return render (request, 'index.html')


