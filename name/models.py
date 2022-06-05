from datetime import datetime
from tokenize import Name
from django.db import models
# Create your models here.

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=30)
    text = models.TextField()
    phone = models.CharField(max_length=12)

    time = models.DateTimeField()
    
    def __str__(self):
        return self.name