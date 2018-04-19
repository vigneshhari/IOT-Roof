from django.db import models

# Create your models here.

class node1(models.Model):
    key = models.CharField(max_length = 500)
    val = models.CharField(max_length = 500)
    time = models.DateTimeField()

class node2(models.Model):
    key = models.CharField(max_length = 500)
    val = models.CharField(max_length = 500)
    time = models.DateTimeField()
    
class lock(models.Model):
    lock = models.CharField(max_length = 500 )
