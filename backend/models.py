from django.db import models


class CategoryDB(models.Model):
    category = models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Image = models.ImageField(upload_to="Category Image", null=True, blank=True)

    def __str__(self):
        return self.category


class BooksDB(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="Books Image", null=True, blank=True)

    def __str__(self):
        return self.name

class BackendUserDB(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name