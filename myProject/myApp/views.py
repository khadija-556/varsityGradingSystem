from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from myApp.models import *
from myProject.forms import *

# Create your views here.

def singupPage(request):
    if request.method == 'POST':
        form=customUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("singinPage")
    else:
        form=customUserForm()
        return render(request,"singupPage.html",{'form':form})


def singinPage(request):
    if request.method == 'POST':
        form=CustomerAutenticationForm(request,data=request.POST)
        if form.is_valid():
           
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            
            user=authenticate(username =username,password = password)
            login(request,user)
            return redirect("Student_ModelAdd")
    else:
            form=CustomerAutenticationForm()

    return render(request,"singin.html",{'form':form})
def logoutPage(request):
    logout(request)
    return redirect("singinPage")


def myDashboard(request):
    return render(request,'dashboard.html')




##Versity grading
def subjectAdd(request):
    
    if request.method == "POST":
        form=subjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("subjectAdd")
    else:
        form=subjectForm()
        
    return render(request,"subjectAdd.html",{'form':form})

def Student_ModelAdd(request):
    
    if request.method == "POST":
        form=Student_ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Student_ModelAdd")
    else:
        form=Student_ModelForm()
        
    return render(request,"Student_ModelAdd.html",{'form':form})

def ViewStudent(request):
    student=Student_Model.objects.all()
    return render(request,"viewStudent.html",{'student':student})



def Grading(request):
    
    if request.method == "POST":
        form=gradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Grading")
    else:
        form=gradeForm()
        
    return render(request,"Grading.html",{'form':form})

def viewMarksPage(request, student_id):
    student = Student_Model.objects.get(pk=student_id)
    marks = grade.objects.filter(student=student)
    total_credit = 0
    total_grade_point = 0
    cgpa=0

    for mark in marks:
        subject_credit = int(mark.subject.credit) 

        if mark.marks >= 40:
            if mark.marks >= 75:
                grade_point = 3.75
            elif mark.marks >= 70:
                grade_point = 3.50
            elif mark.marks >= 65:
                grade_point = 3.25
            elif mark.marks >= 60:
                grade_point = 3.00
            elif mark.marks >= 55:
                grade_point = 2.75
            elif mark.marks >= 50:
                grade_point = 2.50
            elif mark.marks >= 45:
                grade_point = 2.25
            else:
                grade_point = 2.00
            total_credit += subject_credit
            total_grade_point += subject_credit * grade_point
            cgpa=total_grade_point/total_credit

    context = {
        'student': student,
        'marks': marks,
        'total_credit': total_credit,
        'total_grade_point': total_grade_point,
        'cgpa':cgpa
    }

    return render(request, 'viewMarksPage.html', context)