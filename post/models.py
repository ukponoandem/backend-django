from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  author = models.CharField(max_length=255)
  published_date = models.DateField(null=True)
  
  
def __str__(self):
    return f"{self.title} - {self.author}"
# Create your models here.
