from django.db import models

# Create your models here.

class student_model(models.Model):
    student_name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    physics_mark=models.IntegerField()
    chemistry_mark=models.IntegerField()
    maths_mark=models.IntegerField()
    computer_science_mark=models.IntegerField()