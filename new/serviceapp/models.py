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
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.user_id,self.role,self.location,self.full_name,self.email}"


class ServiceCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category_id,self.category_name,self.description}"


class Worker(models.Model):
    worker_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    worker_address= models.CharField(max_length=200 ,null=True, blank=True)

    def __str__(self):
        return self.full_name


class WorkerService(models.Model):
    worker_service_id = models.AutoField(primary_key=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    category = models.ForeignKey('ServiceCategory', on_delete=models.CASCADE)
    rate_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.worker} - {self.category} @ {self.rate_per_hour}/hr"
    

class RequestStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=50)

    def __str__(self):
        return self.status_name


class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    consumer = models.ForeignKey('User', on_delete=models.CASCADE)
    worker = models.ForeignKey('Worker', on_delete=models.CASCADE)
    category = models.ForeignKey('ServiceCategory', on_delete=models.CASCADE)
    status = models.ForeignKey('RequestStatus', on_delete=models.CASCADE)
    scheduled_date = models.DateField()

    def __str__(self):
        return f"Request {self.request_id} - {self.consumer} -> {self.worker} ({self.status})"   


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    request = models.ForeignKey('Request', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)       

    def __str__(self):
        return f"Payment {self.payment_id} - {self.amount} ({self.payment_status})"  
    

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    request = models.ForeignKey('Request', on_delete=models.CASCADE)
    consumer = models.ForeignKey('User', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Review {self.review_id} - {self.rating}★ by {self.consumer}"    
    

class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification to {self.user} - {self.title}"    