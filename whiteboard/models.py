from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=50)

class Engineer(models.Model):
    engineer_name = models.CharField(max_length=50)
    engineer_no = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    sales = models.ForeignKey(User, on_delete=models.CASCADE)
    engineer_type = models.CharField(max_length=50, default='正社員')
    engineer_status = models.CharField(max_length=20, default='勤務中')
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)