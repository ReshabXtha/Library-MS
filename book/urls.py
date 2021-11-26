from django.urls import path
from . import views

urlpatterns = [

    path('', views.book, name='book'),
    path('<int:ids>/issue_book', views.issueBook, name='issueBook'),
    path('submitIssuedBook', views.SubmitIssuedBook.as_view(), name='submitIssuedBook'),
    path('requestBook', views.requestBook, name='requestBook'),
    path('submit', views.requestSubmit, name='submitRequest'),
    path('addbook', views.addBook, name='addBook'),
    # path('<int:ids>return', views.delete, name='return'),
    path('issuedbook', views.issuedBook, name='issuedbook'),
    path('submitAddBook', views.submitAddBook, name='submitAddBook')
]
