from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

class Status:
    solved = 0
    pending = 1

class Post(models.Model):
    title = models.CharField(max_length=100)
    body= models.TextField()
    date = models.DateField()
    #labels = models.CharField(max_length=)

    #def __init__(self, student: Student):
        #self.student = student
        #self.status = Status.pending

