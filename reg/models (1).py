from django.db import models
from django.utils.text import slugify

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)
    mob_no = models.IntegerField()
    institution = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Online_branch(models.Model):
    bid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    image = models.ImageField(blank=True, upload_to="images/")
    

    def __str__(self):
        return self.title




class Newsletter(models.Model):
    newsletter_id = models.CharField(primary_key=True, max_length=10)
    title = models.CharField(max_length=1000)
    description = models.TextField()
    videos1 = models.FileField(blank=True,upload_to="videos1/")
   
    def __str__(self):
       return self.title
class Newsletter_videos1(models.Model):
    newsletter_id = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
   
    videos1 = models.FileField(upload_to="videos1/")

    def __str__(self):
        return str(self.newsletter_id)





