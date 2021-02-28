from django.shortcuts import render, HttpResponse, redirect
from books_authors_app.models import Book, Publisher

def index(request):
    context={
    "libro" : Book.objects.all()
    }
    return render (request, 'libros.html',context)

def index_uno(request):
    
    context={
    "author" : Publisher.objects.all()
    }
    return render (request, 'autores.html',context)

def create(request):
        booking = Book(title=request.POST['nombre'], descripcion=request.POST['descripcion'])
        booking.save()
        return redirect('/libros')

def created(request):
        escritor = Publisher(name=request.POST['nombre'], note=request.POST['note'])
        escritor.save()
        return redirect('/autores')

def info_libros (request, number):
    aut_all = Publisher.objects.all()
    libro = Book.objects.get(id=number)
    aut = libro.publishers.all() 
    context={
        "libro" : libro,
        "publishers" : aut,
        "autores" : aut_all
    }
    return render(request, 'info_libro.html',context)

def info_autor (request, number):
    libros_all = Book.objects.all()
    autor = Publisher.objects.get(id=number)
    boo = autor.books.all() 
    context={
        "autor" : autor,
        "libros" : boo,
        "libros1" : libros_all
    }
    return render(request, 'info_autor.html',context)

def agregar_autor(request, number):
    libro = Book.objects.get(id=number) #informacion que se extrae de la bd
    id_aut = request.POST['id_autor'] #es solo un numero
    name_autor = Publisher.objects.get(id=id_aut)
    name_autor.books.add(libro) #se agrega el libro al autor y viceversa
    return redirect(f'/info_libros/{number}') #redirect a la misma pagina.


def agregar_libro(request, number):
    autor = Publisher.objects.get(id=number) #informacion que se extrae de la bd
    id_book = request.POST['id_book'] #es solo un numero
    name_book = Book.objects.get(id=id_book)
    name_book.publishers.add(autor) #se agrega el libro al autor y viceversa
    return redirect(f'/info_autor/{number}') #redirect a la misma pagina.

def home(request):
    return render(request, 'home.html')








'''def agregar_libros(request):
    booking=request.POST["nombre"]
    descripcion=request.POST["descripcion"]
    Book.objects.create(title=booking, descripcion=descripcion)
    context={
        "new_books": Book.objects.all()
    }
    return redirect('libros')'''



    