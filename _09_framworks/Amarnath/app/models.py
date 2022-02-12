from django.db import models
from datetime import datetime


# Create your models here.
class Documents(models.Model):
    Title = models.CharField(max_length=25)
    Description = models.TextField()
    Attachments = models.FileField(upload_to="Files/")
    Signature = models.CharField(max_length=15)
    datetime = models.DateField(default=datetime.now)

    def __str__(self):
        return self.Title

   

