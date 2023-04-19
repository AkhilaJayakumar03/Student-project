
from django import forms

class student_form(forms.Form):
    student_name=forms.CharField(max_length=50)
    date_of_birth=forms.DateField()
    physics_mark=forms.IntegerField()
    chemistry_mark=forms.IntegerField()
    maths_mark=forms.IntegerField()
    computer_science_mark=forms.IntegerField()