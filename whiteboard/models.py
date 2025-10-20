from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=50)

class Engineer(models.Model):
    engineer_name = models.CharField(max_length=50)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    sales_name = models.ForeignKey(User, on_delete=models.CASCADE)
    engineer_type = models.CharField(max_length=50)