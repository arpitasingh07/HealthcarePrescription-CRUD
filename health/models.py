from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Prescription(models.Model):
    p_name= models.CharField(max_length=100)
    p_id= models.CharField(max_length=25)
    p_img= models.ImageField(upload_to='pics/')
    p_contact= models.BigIntegerField()
    p_dob= models.CharField(max_length=60)
    p_age= models.IntegerField()
    p_gender= models.CharField(max_length=10)
    p_diagnosed= models.TextField()
    p_blood= models.FloatField()
    p_rate= models.FloatField()
    p_height= models.FloatField()
    p_weight=models.FloatField()
    p_allergies= models.TextField()
    p_health= models.TextField()
    p_city= models.CharField(max_length=200)
    p_address= models.TextField()
    p_drug= models.TextField()
    p_unit= models.TextField()
    p_dosage= models.TextField()
    p_check=models.CharField(max_length=4)
    present_date=models.TextField()
    

    

   
    
    


    class Meta:
        db_table="health_prescription"

