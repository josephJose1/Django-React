from django.db import models

# Create your models here.
class Note(models.Model):
    body = models.TextField(null=True, blank=True) # WE ARE ABLE to submit this values
    update = models.DateTimeField(auto_now=True)
    creates = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]#first 
