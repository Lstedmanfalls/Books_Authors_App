from django.shortcuts import render, redirect, HttpResponse
from .models import Books, Authors

def index(request):
    context = {
    "all_the_books": Books.objects.all(),
    }
    return render(request, "index.html", context)

def create_book(request):
    if request.method != "POST":
        return redirect("/")
    if request.method == "POST":
        Books.objects.create(title = request.POST["title"], desc = request.POST["desc"])
    return redirect("/")

def book_profile(request, book_id):
    this_book = Books.objects.get(id=book_id)
    context = {
    "a_book": this_book,
    "all_the_authors":Authors.objects.all()
    }
    return render(request, "book_profile.html", context)

def add_author(request, book_id):
    if request.method != "POST":
        return redirect("/")
    this_book = Books.objects.get(id=book_id)
    this_author = Authors.objects.get(id=request.POST["author_id"])
    this_book.book_authors.add(this_author)
    return redirect(f"/books/{book_id}")
    
def author(request):
    context = {
    "all_the_authors": Authors.objects.all(),
    }
    return render(request, "authors.html", context)

def create_author(request):
    if request.method != "POST":
        return redirect("/authors")
    if request.method == "POST":
        Authors.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"])
    return redirect("/authors")

def author_profile(request, author_id):
    this_author = Authors.objects.get(id=author_id)
    context = {
    "an_author": this_author,
    "all_the_books":Books.objects.all()
    }
    return render(request, "author_profile.html", context)

def add_book(request, author_id):
    if request.method != "POST":
        return redirect("/authors")
    this_author = Authors.objects.get(id=author_id)
    this_book = Books.objects.get(id=request.POST["book_id"])
    this_author.books.add(this_book)
    return redirect(f"/authors/{author_id}")