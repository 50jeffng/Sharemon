from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

class Status:
    solved = 0
    pending = 1

class Post(models.Model):
    title = models.CharField(max_length=100)
    body= models.TextField()
    date = models.DateField()
    slug = models.SlugField()
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, null=True)

    RESOLVED = 1
    PENDING = 2
    STATUS_CHOICES = (
        (RESOLVED, 'resolved'),
        (PENDING, 'pending')

    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + "..."

    #labels = models.CharField(max_length=)

    #def __init__(self, student: Student):
        #self.student = student
        #self.status = Status.pending

class LostAndFound(Post):
    item = models.CharField(max_length=50, null=True, blank=True)

