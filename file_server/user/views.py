from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.db import models
from .models import *
from rest_framework.decorators import action

# Create your views here.
class UserView(APIView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            userId = request.POST['userId']
            userToken = request.POST['userToken']
            user = User.objects.get(userId = userId)
            if user:
                if userToken != '': #user에 토큰 입
                    user.userToken = userToken
                    user.save()
                    return HttpResponse('token_enroll_success')
                return HttpResponse('/user_enroll_failure')

            user = User(userId=userId)
            user.save()
            return HttpResponse('userId_enroll_success', user)

        return HttpResponse('/user_enroll_failure')