from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class Custom_user(AbstractUser):
    Department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

class studentModel(models.Model):
    firstname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstname
    
class subjectModel(models.Model):
    subject_name=models.CharField(max_length=100,null=True,)
    student_code=models.CharField(max_length=100,null=True)
    credit=models.IntegerField(null=True)
    def __str__(self) -> str:
        return self.subject_name

    
class Student_Model(models.Model):
    gender=[
        ('male','Male'),
        ('female','Female')
    ]
    name=models.CharField(max_length=100,null=True)
    age=models.IntegerField()
    depertment=models.CharField(max_length=120,null=True)
    subject=models.ManyToManyField(subjectModel,null=True)
    gender=models.CharField(choices=gender,null=True,max_length=120)
    def __str__(self) -> str:
        return self.name


class grade(models.Model):
    subject=models.ForeignKey(subjectModel,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student_Model,on_delete=models.CASCADE,null=True)
    marks=models.IntegerField()
    
    letter_grade = models.CharField(max_length=2, blank=True)
    def __str__(self) -> str:
        return self.student.name


class MarkModel(models.Model):
    student = models.ForeignKey(Student_Model, on_delete=models.CASCADE)
    subject = models.ForeignKey(subjectModel, on_delete=models.CASCADE)
    marks = models.FloatField()


