from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello(request):
    text="""<h1> Welcome to my app </h1>"""
    return HttpResponse(text)

def hello(request):
   return render(request, "hello.html", {})


def hello2(request,id):
   text = "Displaying article Number : %s"%id
   return HttpResponse(text)

def hello3(request,id):
   return render(request, "hello2.html", {"n" : id, "days":["mon","tue","wed"]})

from myapp.models import Dreamreal

def crudops(request):
   #Creating an entry
    #Read ALL entries
   objects = Dreamreal.objects.all()
   res ='Printing all Dreamreal entries in the DB : <br>'
   
   for elt in objects:
      elt.delete()
   
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   print(dreamreal)

   #Read ALL entries
   objects = Dreamreal.objects.all()
   res ='Printing all Dreamreal entries in the DB : <br>'
   
   for elt in objects:
      res += elt.name+"<br>"
   
   #Read a specific entry:
   sorex = Dreamreal.objects.get(name = "sorex")
   res += 'Printing One entry <br>'
   res += sorex.name
   
   #Delete an entry
   res += '<br> Deleting an entry <br>'
   sorex.delete()
   
   #Update
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   res += 'Updating entry<br>'
   
   dreamreal = Dreamreal.objects.get(name = 'sorex')
   dreamreal.name = 'thierry'
   dreamreal.save()
   
   return HttpResponse(res)

from myapp.forms import LoginForm

def login(request):
   username = "not logged in"
   
   # request.method: type of HTML action , GET or PUT or POST etc
   if request.method == "POST":
      #Get the posted form
	  # request.POST : gets the data from html page
      print("Get data from HTML")
      MyLoginForm = LoginForm(request.POST)
      username = MyLoginForm.data.get('username')
	  #Debugging
      #print( MyLoginForm.errors)
     # print("Login user:",username, " ",MyLoginForm.is_valid())
     # MyLoginForm.clean_message()
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
         print("Login user:",username)
   else:
      print(" no POST")
      MyLoginForm = Loginform()
		
   return render(request, 'loggedin.html', {"username" : username})