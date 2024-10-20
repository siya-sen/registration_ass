
from django.db import models

class Registration(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    DateOfBirth = models.DateField()
    PhoneNumber = models.CharField(max_length=15)
    Gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    RegistrationDate = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return self.Name
