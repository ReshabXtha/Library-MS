from django.contrib import admin
from .models import Book
from .models import IssuedBook
from .models import RequestBook

admin.site.register(Book)
admin.site.register(IssuedBook)
admin.site.register(RequestBook)
