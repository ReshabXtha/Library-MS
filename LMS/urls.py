from django.contrib import admin
from django.urls import path, include
from . import views
# from book import views as book_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login/', views.login_, name='login'),
    path('book/', include('book.urls'), name='book'),
    path('student/', include('Student.urls'), name='student'),
]
