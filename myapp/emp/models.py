from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200, unique=True)  # Ensure emp_id is unique
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=15)