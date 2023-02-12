from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse("Страница приложения Job list")

def categories(request, catid):
    if request.POST:
        print(request.POST)

    return HttpResponse (f"<h1> статьи по категориям </h1><p>{catid}</p>")

def archieve(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)


    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def PageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')