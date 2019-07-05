from django.contrib import admin

from home.models import Student
from home.models import Teacher
from home.models import Marks
from home.models import Library
from home.models import Section

# Register your models here.

# admin.site.register(Student)
# admin.site.register(Teacher)
# admin.site.register(Marks)
# admin.site.register(Library)
# admin.site.register(Section)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ('student_name','id')
    list_filter = ('student_name','department','timestamp')
    fields = ('student_name','department')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    pass

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    pass
