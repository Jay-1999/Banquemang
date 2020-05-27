from django.db import models

# Create your models here.
class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=20,unique=True)
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=25)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email_id = models.CharField(max_length=30,unique=True)
    mobile_no = models.IntegerField(max_length=10,unique=True)
    address = models.TextField()
    city_id = models.ForeignKey(City,on_delete=models.CASCADE)
    pincode = models.IntegerField(max_length=6)
    id_proof_doc_path = models.FileField(upload_to='owner_id',null=True)
    password = models.CharField(max_length=100)
    reg_date_time = models.DateTimeField(auto_now_add=True)
    login_date_time = models.DateTimeField(auto_now_add=True,null=True)
    active_status = models.BooleanField(default=False)
