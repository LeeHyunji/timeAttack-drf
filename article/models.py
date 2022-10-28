from operator import mod
from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    title = models.CharField(max_length=255)
    content = models.TextField()