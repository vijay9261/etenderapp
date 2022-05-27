from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from datetime import date

class Admins(models.Model):  
    fname = models.CharField(max_length=255)  
    lname = models.CharField(max_length=255)  
    username  = models.CharField(max_length=255)  
    password  = models.CharField(max_length=255)  
    email  = models.CharField(max_length=255)  
    phone  = models.CharField(max_length=255)  
    class Meta:  
        db_table = "admins" 

class Companies(models.Model):  
    name = models.CharField(max_length=255)  
    email  = models.CharField(max_length=255)  
    mobile  = models.CharField(max_length=255)  
    company_name  = models.CharField(max_length=255)  
    company_phone  = models.CharField(max_length=255)  
    company_address  = models.CharField(max_length=255)  
    username  = models.CharField(max_length=255)  
    password  = models.CharField(max_length=255)  
    class Meta:  
        db_table = "companies" 

class Tenders(models.Model):  
    title = models.CharField(max_length=255)  
    description  = models.TextField()  
    budget  = models.CharField(max_length=255)  
    tender_close_date  = models.DateField(null=True, blank=True) 
    company_id = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:  
        db_table = "tenders" 
    @property
    def is_past_date(self):
        return date.today() > self.tender_close_date
    
class TenderAppliers(models.Model):  
    name = models.CharField(max_length=255)  
    email  = models.CharField(max_length=255)  
    mobile  = models.CharField(max_length=255)  
    company_name  = models.CharField(max_length=255)  
    company_phone  = models.CharField(max_length=255)  
    company_address  = models.CharField(max_length=255)  
    bid_amount  = models.CharField(max_length=255)  
    tender_id = models.IntegerField()
    applied_date = models.DateTimeField(auto_now_add=True, blank=True)
    given_to=models.BooleanField(default=False)
    class Meta:  
        db_table = "tender_appliers"