from operator import truediv
from unittest.util import _MAX_LENGTH
from django.db import models

class Post(models.Model):
    Choices=[['published','p'],['draft','d']]
    title = models.CharField(max_length=200)
    DT=models.DateTimeField(null=True)
    Author=models.CharField(max_length=30)
    Content=models.TextField()
    Status=models.CharField(max_length=10,choices=Choices)
    IMG=models.ImageField(null=True,blank=True,upload_to="images/")
