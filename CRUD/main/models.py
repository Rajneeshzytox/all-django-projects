from django.db import models

# Create your models here.

class StuData(models.Model):
    class_choices = [
        ('class 6', 'class 6'),
        ('class 7', 'class 7'),
        ('class 8', 'class 8'),
        ('class 9', 'class 9'),
        ('class 10', 'class 10'),
        ('class 11', 'class 11'),
        ('class 12', 'class 12')
    ]

    stu_name = models.CharField(max_length=20)
    roll_no = models.SmallIntegerField()
    stu_class = models.TextField(choices=class_choices)
    gender = models.TextField(choices=[('male','male'), ('female', 'female')])
    dob = models.DateField()
    date_of_entry = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.roll_no} {self.stu_name}'