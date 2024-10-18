from django.db import models

# Create your models here.

class contactForms(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Subject = models.CharField(max_length=100)
    Message = models.CharField(max_length=500)
