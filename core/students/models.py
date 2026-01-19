from django.db import models

# Create your models here.

class Student(models.Model):
    roll = models.IntegerField()
    stud_name = models.CharField(max_length=100)
    per = models.FloatField()
    photo = models.FileField(upload_to='images')