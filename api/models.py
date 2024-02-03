from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Investor(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField()
    
    def __str__(self):
        return self.user.username
    

class Startup(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField()
    company_name = models.CharField(blank=False,max_length=50)
    business_description = models.CharField(blank=False,max_length=1500)
    revenue = models.FloatField(blank=False)
    interested = models.ManyToManyField(Investor,blank=True)
    csv_file = models.FileField(upload_to='media',blank=True)
    def __str__(self):
        return self.company_name
    
    def approve(self):
        pass
