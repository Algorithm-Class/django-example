from django.db import models

# Create your models here.
class Dreamreal(models.Model):

   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   name = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()

   class Meta:
      db_table = "dreamreal"

   def __str__(self):
	   return str(self.website)+str(self.mail)+str(self.name)
