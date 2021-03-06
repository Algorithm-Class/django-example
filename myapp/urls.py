from django.contrib import admin
from django.urls import path,re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    #'myapp.views',
    #path('admin/', admin.site.urls),
	path('',  views.hello,name='hello1'),
    re_path('display(\d+)',  views.hello2,name='id'),
	path('crud',  views.crudops,name='crud'),
	re_path('temp(\d+)',  views.hello3,name='id'),
	path(r'connection/',TemplateView.as_view(template_name = 'login.html')),
	path(r'^login/', views.login, name = 'login'),

]