from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")
def root(request):
    return redirect("/blogs")
def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")
def create(request):
    return redirect("/")
def show(request, number):
    return HttpResponse(f"placeholder para mostrar el blog numero: {number}")
def edit(request, number):
    return HttpResponse(f"placeholder para editar el blog {number}")
def destroy(request, number):
    return redirect("/blogs")
def index1(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)