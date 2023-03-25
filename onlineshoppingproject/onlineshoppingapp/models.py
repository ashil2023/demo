from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField 

class Profile(models.Model):
    name1 = models.CharField(max_length=250)
    img1 = models.ImageField(upload_to='pics')
    desc1=models.TextField (max_length=2000)


def __str__(self):
        return  self.name1