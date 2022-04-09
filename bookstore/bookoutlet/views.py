from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg
from django.http import Http404

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "bookoutlet/index.html", {
        "books": books,
        "total_number_of_the_books": num_books,
        "average_rating":avg_rating,
    })

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "bookoutlet/book_detail.html", {
        "title": book.title,
        "rating": book.rating,
        "author": book.author,
        "is_bestselling": book.is_bestselling,
    })

