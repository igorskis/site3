from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index/index.html')


def books(request):
    return render(request, "index/books.html")


def certificates(request):
    return render(request, "index/certificates.html")
