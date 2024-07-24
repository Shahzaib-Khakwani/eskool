from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


# Create your models here.


def image_student_path(instance, filename):   
    return f'user/{instance.name}/student/{filename}'

class Student(models.Model):
    ORPHAN_CHOICES = (
        ("Yes", "yes"),
        ("No", "no"),
    )
    OCS_CHOICES = (
        ("Yes", "yes"),
        ("No", "no"),
    )
    GENDER_CHOICES = (
        ("Male", "male"),
        ("Female", "female"),
    )
    RELIGION_CHOICES = (
        ("Athiest", "Athiest"),
        ("Religion", "religion"),
    )
    BLOOD_CHOICES = (
        ("A", "A"),
        ("A-", "A-"),
        ("B", "B"),
        ("B-", "B-"),
        ("AB", "AB"),
        ("AB-", "AB-"),
    )

    # user = models.OneToOneField(User, related_name='students', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    registration = models.CharField(max_length=50, unique=True)
    studentClass = models.ForeignKey('eClass.eClass', related_name='students', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_student_path, null=True, blank=True)
    DateOFAdmission = models.DateField()
    discountPercentage = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    phoneNumber = models.PositiveIntegerField(null=True, blank=True)
    DateOFBirth = models.DateField(null=True, blank=True)
    birthIDNumber = models.PositiveIntegerField(null=True, blank=True , unique=True)
    orphanStatus = models.CharField(max_length=3, choices=ORPHAN_CHOICES, null=True, blank=True)
    bloodGroup = models.CharField(max_length=3, choices=BLOOD_CHOICES, null=True, blank=True)
    religion = models.CharField(max_length=10, choices=RELIGION_CHOICES, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    cast = models.CharField(max_length=100, null=True, blank=True)
    identificationMarks = models.CharField(max_length=100, null=True, blank=True)
    prevSchoolName = models.CharField(max_length=100, null=True, blank=True)
    prevID = models.CharField(max_length=50, null=True, blank=True , unique=True)
    disease = models.CharField(max_length=50, null=True, blank=True)
    totalSiblings = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    fatherName = models.CharField(max_length=100)
    fatherID = models.CharField(max_length=50, unique=True)
    fatherOccupation = models.CharField(max_length=100)
    fatherEducation = models.CharField(max_length=100)
    fatherProfession = models.CharField(max_length=100)
    fatherPhoneNumber = models.PositiveIntegerField(null=True, blank=True)
    fatherIncome = models.PositiveIntegerField(null=True, blank=True)
    motherName = models.CharField(max_length=100)
    motherID = models.CharField(max_length=50, unique=True)
    motherOccupation = models.CharField(max_length=100)
    motherEducation = models.CharField(max_length=100)
    motherProfession = models.CharField(max_length=100)
    motherPhoneNumber = models.PositiveIntegerField(null=True, blank=True)
    motherIncome = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
