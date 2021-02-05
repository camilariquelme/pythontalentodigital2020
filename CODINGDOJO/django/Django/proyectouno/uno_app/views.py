from django.shortcuts import render, HttpResponse

def first_view(request):
    return HttpResponse("this method is the first view in uno_app")

def second_view(request):
    return HttpResponse("this method is the second view in uno_app")