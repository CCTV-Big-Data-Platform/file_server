from django.db import models


class File(models.Model):
    def user_directory_path(instance, file):
        print("INSTANCE" , instance)
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return '{0}/{1}'.format(instance.userName,file)

    userName = models.CharField(max_length=100)  # name is filename without extension
    upload_date = models.DateTimeField(auto_now=True, db_index=True)
    file = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.userName