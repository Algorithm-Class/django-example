from django.db import models

# Create your models here.
class Student(models.Model):

   name = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   course = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()

   class Meta:
      db_table = "student"

   def __str__(self):
	   return str(self.name)+str(self.phonenumber)+str(self.course)