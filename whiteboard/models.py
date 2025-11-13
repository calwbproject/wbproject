from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.company_name

class Engineer(models.Model):
    
    ENGINEER_TYPE_CHOICES = [
        ('正社員','正社員'), ('私宅','私宅'), ('新卒','新卒'), ('グローバル','グローバル')
    ]
    
    ENGINEER_STATUS_CHOICES = [
        ('今月入社','今月入社'), ('来月入社','来月入社'), ('勤務中','勤務中'), ('今回終了','今回終了'), ('退職予定','退職予定')
    ]
    
    engineer_name = models.CharField(max_length=50)
    engineer_no = models.CharField(max_length=50, null= True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    sales = models.ForeignKey(User, on_delete=models.CASCADE)
    engineer_type = models.CharField(max_length=50, choices=ENGINEER_TYPE_CHOICES ,default='正社員')
    engineer_status = models.CharField(max_length=20, choices=ENGINEER_STATUS_CHOICES, default='勤務中', null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.engineer_name} ({self.engineer_no})"