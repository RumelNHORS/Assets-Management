from django.db import models
from datetime import date

class AssetsModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    ASSETS_CHOICES = (
        ('Phone', 'Phones'),
        ('Tablet', 'Tablets'),
        ('Laptop', 'Laptops'),  
    )
    asset = models.CharField(max_length=10, choices=ASSETS_CHOICES)
    brand = models.CharField(max_length=20)
    quantity = models.IntegerField()
    date = models.DateField(("Date"), default=date.today)
    
    def __str__(self):
        return self.name
    
class CheckIn(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    ASSETS_CHOICES = (
        ('Phone', 'Phones'),
        ('Tablet', 'Tablets'),
        ('Laptop', 'Laptops'),  
    )
    asset = models.CharField(max_length=10, choices=ASSETS_CHOICES)
    checkin_date = models.DateTimeField()
    
    def __str__(self):
        return self.customer_name
    
class CheckOut(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    ASSETS_CHOICES = (
        ('Phone', 'Phones'),
        ('Tablet', 'Tablets'),
        ('Laptop', 'Laptops'),  
    )
    asset = models.CharField(max_length=10, choices=ASSETS_CHOICES)
    checkout_date = models.DateTimeField()
    
    def __str__(self):
        return self.customer_name
