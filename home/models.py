from django.db import models

# Create your models here.

class Teacher(models.Model):
    teacher_id = models.AutoField(verbose_name = "ID", primary_key = True)
    teacher_name = models.CharField(verbose_name = "Teacher Name", max_length = 30)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.teacher_name

class Student(models.Model):
    student_name = models.CharField('Student Name', max_length = 30, null = True)
    dept = (
    ('CSE','Computer Science'),
    ('MECH','Mechanical'),
    ('CV','Civil')
    )
    department = models.CharField('Department', choices = dept, blank = True, null = True, max_length = 30)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.student_name
    

class Marks(models.Model):
    sid = models.ForeignKey('Student', on_delete = models.SET_NULL, null = True)
    sub1 = models.IntegerField(verbose_name = "Subject1")
    sub2 = models.IntegerField(verbose_name = "Subject2")
    sub3 = models.IntegerField(verbose_name = "Subject3")

    # def __str__(self):
    #     s = str(sid)
    #     return self.s
    
class Library(models.Model):
    sid = models.ForeignKey('Student', on_delete = models.SET_NULL, null = True)
    book_name = (
        ('Jp','Java programming'),
        ('Cp','C programming'),
        ('C++p','C++ programming'),
        ('Pp','Python')
    )
    book = models.CharField('Book Name', choices = book_name, blank = True, null = True, max_length = 30)
    due_date = models.DateField(verbose_name = "Due Date", null=False, blank=True)

    def __str__(self):
        return self.book

class Section(models.Model):
    section = models.CharField('Section', max_length=20, null = False)
    advisor = models.OneToOneField("Teacher", on_delete=models.SET_NULL, null = True)
    students = models.ManyToManyField('Student',null = False)

    def __str__(self):
        return self.section