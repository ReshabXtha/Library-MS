from django.contrib import messages
from django.shortcuts import render
from Student.forms import StudentForm
from Student.models import Student
from Student.models import Semester


def addStudent(request):
    form = StudentForm()
    abc = {
        'form': form
    }
    return render(request, 'StudentAdd.html', abc)


def submitAddStudent(request):
    studentName = request.POST["StudentName"]
    studentAddress = request.POST["StudentAddress"]
    studentFaculty = request.POST["StudentFaculty"]
    studentSemester = request.POST["StudentSemester"]
    studentContact = request.POST["StudentContact"]
    studentEmail = request.POST["StudentEmail"]
    studentProfile = request.POST["StudentProfile"]
    addedStudent = Student(StudentName=studentName, StudentAddress=studentAddress,
                           StudentFaculty=studentFaculty, StudentSemester=studentSemester,
                           StudentContact=studentContact, StudentEmail=studentEmail, StudentProfile=studentProfile)
    addedStudent.save()
    messages.add_message(request, messages.SUCCESS, 'Book requested successfully')
    form = StudentForm()
    pop = {
        'form': form
    }
    return render(request, 'StudentAdd.html', pop)


def studentInfo(request):
    sem = Semester.objects.all()
    return render(request, 'StudentInfo.html', {'sem': sem})


def returnStudentInfo(request, ids):
    sem = Semester.objects.get(pk=ids)
    student = Student.objects.filter(StudentSemester=sem)
    return render(request, 'student_display.html', {'student': student})
