from django.urls import path
from . import views

urlpatterns = [

    path('addstudent', views.addStudent, name='addStudent'),
    path('sbmitstudentform', views.submitAddStudent, name='submitStudentForm'),
    path('studentinfo', views.studentInfo, name='studentInfo'),
    path('<int:ids>/returnstudentinfo/', views.returnStudentInfo, name='returnStudentInfo'),

]
