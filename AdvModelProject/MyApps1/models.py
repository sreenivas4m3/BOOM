from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=125)
    email=models.EmailField
    address=models.CharField(max_length=125)
    rollno=models.IntegerField()
    marks=models.IntegerField()


class Teacher(models.Model):
    name = models.CharField(max_length=125)
    email = models.EmailField
    address = models.CharField(max_length=125)
    subject=models.CharField(max_length=125)
    salary=models.FloatField()


class ContactInfo(models.Model):
    name = models.CharField(max_length=125)
    email = models.EmailField
    address = models.CharField(max_length=125)
    class Meta:
        abstract=True
class Student(ContactInfo):
    rollno = models.IntegerField()
    marks = models.IntegerField()

class Teacher(ContactInfo):
    subject = models.CharField(max_length=125)
    salary = models.FloatField()



class BasicModel(models.Model):
    f1 = models.CharField(max_length=64)
    f2 = models.CharField(max_length=64)
    f3 = models.CharField(max_length=64)

class StandardModel(BasicModel):
    f4 = models.CharField(max_length=64)
    f5 = models.CharField(max_length=64)

class person(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()

class Employee(person):
    eno = models.IntegerField()
    esal = models.FloatField()

class Manager(Employee):
    exp = models.IntegerField()
    team_size = models.IntegerField()


class Parent1(models.Model):
    parent1_id = models.AutoField(primary_key=True)
    f1 = models.CharField(max_length=64)
    f2 = models.CharField(max_length=64)


class Parent2(models.Model):
    parent2_id = models.AutoField(primary_key=True)
    f3 = models.CharField(max_length=64)
    f4 = models.CharField(max_length=64)


class Child(Parent1, Parent2):
    f5 = models.CharField(max_length=64)
    f6 = models.CharField(max_length=64)


class Employees(models.Model):
	eno = models.IntegerField()
	ename = models.CharField(max_length = 64)
	esal = models.FloatField()
	eaddr = models.CharField(max_length = 256)


# Custom-Manager
from django.db import models


class CustomManager(models.Manager):
    def get_queryset(set):
        return super().get_queryset().order_by('-eno')


# Create your models here.
class Employees(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=256)
    objects = CustomManager()