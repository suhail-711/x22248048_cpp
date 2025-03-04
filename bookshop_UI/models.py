from django.db import models

class CustomerQuery(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

class UserAccount(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name


class CartDetails(models.Model):
    customer_name = models.CharField(max_length=100,null=True,blank=True)
    book = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    total = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.customer_name

  

