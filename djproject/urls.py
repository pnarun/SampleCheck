"""djproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


from account.views import home_view,user_login,register,user_logout

from home.views import index
# from home.views import homepage,contact,about,deletestudent,editstudent,createstudent
# from home import views

urlpatterns = [
    path('',home_view, name = 'home'),


    path('login/', user_login, name = 'login'),
    path('logout/', user_logout, name = 'logout'),
    path('register/', register, name = 'register'),
    path('index/', index, name = 'index'),


    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),



    # path('delete-student/<id>', deletestudent),
    # path('edit-student/<id>', editstudent),
    # path('create-student/', createstudent),
]
