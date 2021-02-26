from django.shortcuts import render
from books_app.models import *
# Create your views here.
def index(request):
    
    context = {"authors": Author.objects.all()}		# sólo se envía todos los autores
    return render(request, "first_view.html", context)