from django.db import models

# creating a model which contains the fields of your database

class Student(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.IntegerField()
    std=models.IntegerField()
    email=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.CharField(max_length=30)

