from django.db import models

# Create your models here.
from django.db import models

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)  
    role_name = models.CharField(max_length=100, unique=True)  

    def __str__(self):
        return f"{self.role_id,self.role_name}"
    

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.location_id, self.location_name}"


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=150)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE ,null=True, blank=True)
    email = models.EmailField(unique=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user_id,self.location,self.name,self.mobile,self.email}"


class ServiceCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category_id,self.category_name,self.description}"


    





 