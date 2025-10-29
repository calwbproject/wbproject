from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=50)

class Engineer(models.Model):
    engineer_name = models.CharField(max_length=50)
    engineer_no = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sales = models.ForeignKey(User, on_delete=models.CASCADE)
    engineer_type = models.CharField(max_length=50)
    engineer_status = models.CharField(max_length=20)
    start_date = models.DateField()
    end_data = models.DateField()