from django.db import models

class CustomerQuery(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
  

