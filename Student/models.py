from django.db import models


# Faculty = [('BCA', 'BCA'), ('Bsc.CSIT', 'Bsc.CSIT')]
# Semester = [('1st Sem', '1st Sem'), ('2st Sem', '2st Sem'), ('3st Sem', '3st Sem'), ('4st Sem', '4st Sem'),
#             ('5st Sem', '5st Sem'), ('6st Sem', '6st Sem'), ('7st Sem', '7st Sem'), ('8st Sem', '8st Sem')]


# Create your models here.
class Semester(models.Model):
    Semester = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.Semester


class Student(models.Model):

    StudentName = models.CharField(max_length=100)
    StudentAddress = models.CharField(max_length=100)
    # StudentFaculty = models.CharField(max_length=10,choices=Faculty)
    StudentSemester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    StudentContact = models.CharField(max_length=50, default="")
    StudentEmail = models.CharField(max_length=100, default="")
    StudentProfile = models.ImageField(upload_to='Media', null=True, blank=True)

    def __str__(self):
        return self.StudentName
