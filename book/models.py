from datetime import datetime, timedelta
from django.db import models
from Student.models import Student


class Book(models.Model):
    BookName = models.CharField(max_length=100)
    Book_author = models.CharField(max_length=100)
    Publication = models.CharField(max_length=100)
    PublishedDate = models.DateField(max_length=100)

    def __str__(self):
        return str(self.BookName)


class IssuedBook(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    IssuedTo = models.ForeignKey(Student, on_delete=models.CASCADE)
    IssuedDate = models.DateTimeField(default=datetime.now())
    ReturnDate = models.DateTimeField(default=datetime.now()+timedelta(days=7))

    def __str__(self):
        return '{} {} {} {}'.format(self.Book, self.IssuedTo, self.IssuedDate, self.ReturnDate)


class RequestBook(models.Model):
    Book = models.CharField(max_length=100)
    BookAuthor = models.CharField(max_length=100,null=True, blank=True)
    BookPublication = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.Book)
