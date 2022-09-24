from django.db import models

# Create your models here.
class Note(models.Model):
    body = models.TextField(null=True, blank=True) # WE ARE ABLE to submit this values
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]#first 

    class Meta:
        ordering = ['-updated'] #menus before word reverse