from django.db import models

# Create your models here.
class Notification(models.Model):
    noti_id = models.AutoField(primary_key=True)  # name is filename without extension
    noti_type = models.CharField(max_length=50)
    user = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_created=True)
