from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)


class School_Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.IntegerField()
    contact = models.IntegerField()

    def __str__(self):
        return self.name