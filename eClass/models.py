from django.db import models
from django.core.validators import MinValueValidator
from teacher.models import Teacher

from django.contrib.auth.models import User
# Create your models here.



class eClass(models.Model):
    user = models.ForeignKey(User, related_name='classes', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    monthlyFee = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    teacher = models.ForeignKey(Teacher, related_name='classes', on_delete=models.CASCADE)

    def boys_count(self):
        return self.students.filter(gender = 'Male').count()
    

    def girls_count(self):
        return self.students.filter(gender = 'Female').count()
    

    def total_count(self):
        return self.students.count()

    def __str__(self):
        return self.name