from django import forms
from myApp.models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class customUserForm(UserCreationForm):
    class Meta:
        model=Custom_user
        fields=UserCreationForm.Meta.fields + ('Department','city')

class studentForm(forms.ModelForm):

    class Meta:
        model=studentModel
        fields=['firstname','username','Department','city']
        lables={
            'firstname':'Enter your name',
            'username':'Enter your username',
            'Department':'Enter your depertmant',
            'city':'Enter your city',
        }
class CustomerAutenticationForm(AuthenticationForm):
    class Meta:
        model=Custom_user
        fields=['username','password']

class subjectForm(forms.ModelForm):
    class Meta:
        model=subjectModel
        fields=('__all__')

class Student_ModelForm(forms.ModelForm):
    class Meta:
        model=Student_Model
        fields=('__all__')

class gradeForm(forms.ModelForm):
    class Meta:
        model=grade
        fields=('__all__')

class viewStudent(forms.ModelForm):
    class Meta:
        model=Student_Model
        fields=('__all__')
        
class MarkCreationForm(forms.ModelForm):
    class Meta:
        model = MarkModel
        fields = ['student', 'subject', 'marks']