from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.db import models
from .models import *
from annoying.functions import get_object_or_None

# Create your views here.
class UserView(APIView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            userId = request.POST['userId']
            userToken = request.POST['userToken']
            print("ALL USER : ", User.objects.all())

            user = get_object_or_None(User, userId=userId)
            print("user : ", user)
            if user != None:
                print(user)
                if userToken != '': #user에 토큰 입
                    user.userToken = userToken
                    user.save()
                    return HttpResponse('token_enroll_success')
                return HttpResponse('/user_enroll_failure')

            user = User(userId=userId)
            user.save()
            return HttpResponse('userId_enroll_success', user)

        return HttpResponse('/user_enroll_failure')