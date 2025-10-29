from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10)
    Name = models.CharField(max_length=50)
    Branch = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Name