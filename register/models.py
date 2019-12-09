from django.db import models

# Create your models here.
class User(models.Model):
    username = models.TextField(blank=False,null=False)
    password = models.TextField(blank=False,null=False)


