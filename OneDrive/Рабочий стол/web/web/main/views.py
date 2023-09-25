from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request, "web/main/templates/main.html")

def showauthor(request):
    return render(request, "web/author/templates/author.html")

def showbook(request):
    return render(request, "web/book/templates/book.html")