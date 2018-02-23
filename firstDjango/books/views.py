
'''
## This is before implementing generic views
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.template import loader
from django.shortcuts import render
from django.http import Http404
# Create your views here.
# How the website looks.


def index(request):
    all_books = Book.objects.all()
    template = loader.get_template('books/index.html')
    context = {
        'all_books':all_books
    }
    return render(request,'books/index.html',context)


def detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404('This book does not exist')
    return render(request,'books/detail.html',{'book':book})
'''

from django.views import generic
from .models import Book
from django.views.generic.edit import CreateView


class IndexView(generic.ListView):
    template_name = 'books/index.html'

    def get_queryset(self):
        return Book.objects.all()


class BookCreate(CreateView):
    model = Book
    fields = ['name','author','price','type','book_image']

class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'









