from django.contrib import messages
from django.shortcuts import render, redirect
from book.forms import IssueBookForm, RequestBookForm, AddBookForm
from book.models import Book, RequestBook, IssuedBook
from django.views.generic import CreateView


# Create your views here.

def book(request):
    b = Book.objects.all()
    context = {'books': b}
    return render(request, 'Books.html', context)


def issueBook(request, ids):
    issue_book = Book.objects.filter(pk=ids).last()
    form = IssueBookForm()
    form.fields['Book'].initial = issue_book
    xyz = {
        'form': form,
    }
    return render(request, 'issue_book.html', xyz)


def requestBook(request):
    form = RequestBookForm()
    abc = {
        'form': form
    }
    return render(request, 'Request.html', abc)


def requestSubmit(request):
    bookName = request.POST["Book"]
    bookAuthor = request.POST["BookAuthor"]
    bookPublication = request.POST["BookPublication"]
    requestedBook = RequestBook(Book=bookName, BookAuthor=bookAuthor, BookPublication=bookPublication)
    requestedBook.save()
    messages.add_message(request, messages.SUCCESS, 'Book requested successfully')
    form = RequestBookForm()
    pop = {
        'form': form
    }
    return render(request, 'Request.html', pop)


def addBook(request):
    form = AddBookForm()
    bac = {
        'form': form
    }
    return render(request, 'Addbook.html', bac)


def submitAddBook(request):
    addbookName = request.POST["BookName"]
    bookAuthor = request.POST["Book_author"]
    bookPublication = request.POST['Publication']
    publishedDate = request.POST['PublishedDate']
    addedBook = Book(BookName=addbookName, Book_author=bookAuthor, Publication=bookPublication,
                     PublishedDate=publishedDate)
    addedBook.save()
    form = AddBookForm()
    dod = {
        'form': form
    }
    return render(request, 'Addbook.html', dod)


def submitIssuedBook(request):
    bookName = request.POST["Book"]
    issuedTo = request.POST["IssuedTo"]
    print(bookName)
    submitBook = IssuedBook(Book=bookName, IssuedTo=issuedTo)
    submitBook.save()
    messages.add_message(request, messages.SUCCESS, 'Book issued successfully')
    form = IssueBookForm()
    lol = {
        'form': form
    }
    return render(request, 'issue_book.html', lol)


class SubmitIssuedBook(CreateView):
    template_name = 'issue_book.html'
    form_class = IssueBookForm
    model = IssuedBook

    def form_valid(self, form):
        form.save()
        return redirect('/')


def issuedBook(request):
    b = IssuedBook.objects.all()
    context = {'IssuedBook': b}
    return render(request, 'IssuedBook.html', context)
