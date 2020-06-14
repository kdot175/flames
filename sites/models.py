from django.db import models

# Create your models here.
class details(models.Model):
    his_name = models.CharField(max_length=30)
    her_name = models.CharField(max_length=30)