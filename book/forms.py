from django import forms
from .models import IssuedBook
from .models import RequestBook
from .models import Book


class IssueBookForm(forms.ModelForm):
    class Meta:
        model = IssuedBook
        fields = '__all__'


class RequestBookForm(forms.ModelForm):
    class Meta:
        model = RequestBook
        fields = '__all__'


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
