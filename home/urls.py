from django.urls import path

from . views import *

urlpatterns = [
    path('',home_view,name = 'home'),
    path('delete-student/<id>', deletestudent),
    path('edit-student/<id>', editstudent),
    path('create-student/', createstudent),
]