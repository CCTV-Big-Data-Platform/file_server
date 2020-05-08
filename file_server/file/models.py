from django.db import models


class File(models.Model):
    file = models.FileField()
    userName = models.CharField(max_length=100)  # name is filename without extension
    upload_date = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name