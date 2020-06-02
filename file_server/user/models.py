from django.db import models

class User(models.Model):
    userId = models.CharField(max_length=100, primary_key=True)  # name is filename without extension
    userToken = models.CharField(max_length=500)
