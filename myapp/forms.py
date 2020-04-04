from django import forms
from myapp.models import Dreamreal

class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

   def clean_message(self):
      username = self.data.get("username")
      print("user:",username)
      dbuser = Dreamreal.objects.filter(name = username)
      
      if not dbuser:
         raise forms.ValidationError("User does not exist in our db!")
      else:
         print("Valid user")
      return username