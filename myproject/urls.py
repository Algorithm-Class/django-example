"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from student import views
from django.urls import path,include
#from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
   # path('display/', views.hello,name='hello'),
	path('myapp/', include('myapp.urls')),
	#path('student/', include('student.urls')),
	path('student/',views.StudentList.as_view() ),
]

urlpatterns= format_suffix_patterns(urlpatterns)

