from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=50)

class Engineer(models.Model):
    engineer_name = models.CharField(max_length=50)
    engineer_no = models.CharField(max_length=50)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    sales_name = models.ForeignKey(User, on_delete=models.CASCADE)
    engineer_type = models.CharField(max_length=50)
    engineer_status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)]
                                          ,default=0)
    start_date = models.DateField()
    end_data = models.DateField()