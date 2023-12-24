from django.db import models

# Create your models here.

class Jokes(models.Model):
    desc=models.CharField(max_length=1000)
    def __str__(self):
        return str(self.id)
    
