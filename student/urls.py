from django.contrib import admin
#from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
#from . import views

urlpatterns = [
	path('',views.StudentList.as_view() ),
]

urlpatterns= format_suffix_patterns(urlpatterns)