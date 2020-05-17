from django.db import models
from Banquemng.users.models import City,User

# Create your models here.
class Property_Category(models.Model):
    property_category_id=models.AutoField(primary_key=True)
    property_category_name=models.CharField(max_length=30,unique=True)
class Property(models.Model):
    property_id==models.AutoField(primary_key=True)
    property_category_id=models.ForeignKey(Property_Category,on_delete=models.CASCADE)
    property_name=models.CharField(max_length=30,unique=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    property_identity_doc_path= CharField(max_length=50)
    address = models.TextField()
    city_id = models.ForeignKey(City,on_delete=models.CASCADE)
    pincode = models.IntegerField(max_length=6)
    description= models.TextField()
    capacity=models.IntegerField(max_length=6,null=True)
    normal_price = models.FloatField(max_length=10,null=True)
    decoration_price = models.FloatField(max_length=10,null=True)
    catering_price = models.FloatField(max_length=10,null=True)
    is_property_verified=models.BooleanField(default=False)
    active_status = models.BooleanField(default=False)
class Property_Vid(models.Model):
    property_vid_id = models.AutoField(primary_key=True)
    property_id = models.ForeignKey(Property,on_delete=models.CASCADE)
    property_vid_path= models.CharField(max_length=50)
class Property_Img(models.Model):
    property_img_id = models.AutoField(primary_key=True)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    property_img_path = models.CharField(max_length=50)