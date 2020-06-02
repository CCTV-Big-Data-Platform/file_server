from django.db import models

class User(models.Model):
    userId = models.CharField(max_length=100, primary_key=True)  # name is filename without extension
    userToken = models.CharField(max_length=500)

    # @classmethod
    # def create(cls, userID):
    #     user = cls(userId=userID)
    #     return user
    #
    # @classmethod
    # def setToken(cls, userID, userToken):
    #     user = cls()
