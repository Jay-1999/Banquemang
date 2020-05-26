from django.db import models

# Create your models here.
class Admin(models.Model):
    admin_email_id = models.CharField(max_length=30)
    admin_password = models.CharField(max_length=100)
