from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.IntegerField(null=True)
    Email=models.EmailField()
    dob=models.DateField()
    course=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class course(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    duration=models.CharField(max_length=50)
    timing= models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    def __str__(self):
        return self.title 
