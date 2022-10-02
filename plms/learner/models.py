from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django import forms

# from tkinter import CASCADE
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from django.core import serializers
from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    name = models.CharField(max_length=60)
    tid = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default='')

    class meta:
     verbose_name_plural="1. Teachers"



# Create your models here.
class Course(models.Model):
 title = models.CharField(max_length=50)
 description = models.CharField(max_length=300)
 teacher = models.ForeignKey(Teacher,on_delete=CASCADE)
 enrollkey = models.CharField(max_length=50, unique = True)
 fek = models.CharField(max_length=50,  blank=True, default='')
 cresource = models.FileField(upload_to="",blank=True, default='')
 isteacher = models.CharField(max_length=5,blank=True,default='n')
 

 class meta:
     verbose_name_plural="2. Courses"

class Student(models.Model):
    sid=models.ForeignKey(User,on_delete=models.CASCADE)
    edc=models.ManyToManyField(Course,blank=True,default='')
    isteacher = models.CharField(max_length=5,blank=True,default='n')

    class meta:
     verbose_name_plural="3. Students"


class Csource(models.Model):
    file = models.FileField(null = True)
    fname = models.CharField(max_length=500,default='')
    fid = models.ForeignKey(Course, on_delete=CASCADE)




