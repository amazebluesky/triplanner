from django.db import models

class Post(models.Model):
    image = models.FileField(null=True,blank=True)
 