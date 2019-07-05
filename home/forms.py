from django import forms

from home import models

class StudentEditModelForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__' # student_name, department
        # to edit only one data 
        # field = ('student_name',) or field = ('department') ## it will be in tuple form
        widgets = {
            'student_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Student Name'}),
            'department':forms.Select(attrs={'class':'custom-select'})
        }

class StudentSearchForm(forms.Form):
    q = forms.CharField(label = '',widget = forms.TextInput(attrs = {'class':'form-control','maxlength':'30','placeholder':'Search'}))

class StudentCreateForm(forms.Form):
    student_name = forms.CharField(label='', widget = forms.TextInput(attrs = {'class':'form-control','maxlength':'50','placeholder':'Student Name'}))
    dept = (
        ('CSE','Computer Science'),
        ('ME','Mechanical'),
        ('CV','Civil')
    )
    department = forms.CharField(label="", widget = forms.Select(attrs = {'class':'form_control'}, choices = dept))