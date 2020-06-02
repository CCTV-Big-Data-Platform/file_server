from rest_framework.views import APIView
from django.http import HttpResponse
import requests
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
from firebase_admin import datetime
from django.apps import apps
User = apps.get_model('user', 'User')

cred = credentials.Certificate('./detection/whatsup-ad0b7-firebase-adminsdk-6yhd1-2e4fcd728a.json')
default_app = firebase_admin.initialize_app(cred)
topic = 'detection'


class NotificationView(APIView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            befEncoding = request.POST.get('befEncoding', False)
            timestamp = request.POST.get('timestamp', False)
            userId = request.POST.get('userId', False)
            detectionType = request.POST.get('detectionType',False)
            print("USER : ",userId)
            user = User.objects.get(userId=userId)

            bodyContent = "침입자 발생!!"
            if detectionType == "fire":
                bodyContent = "불났어요 불났어요 삐뽀삐뽀!!"

            message = messaging.Message(
                android=messaging.AndroidConfig(
                    ttl=datetime.timedelta(seconds=3600),
                    priority='normal',
                    notification=messaging.AndroidNotification(
                        title='삐뽀삐뽀',
                        body = bodyContent,
                        icon='',
                        color='#f45342',
                        sound='default'
                    ),
                ),
                data={
                    'byteArray': befEncoding,
                    'timestamp': timestamp
                },
                webpush=messaging.WebpushConfig(
                    notification=messaging.WebpushNotification(
                        title='웹 알림',
                        body='여긴 어떨까',
                        icon='',
                    ),
                ),
                # topic=topic
                token=user.userToken
            )

            response = messaging.send(message)
            # Response is a message ID string.
            print('Successfully sent message:', response)

            return HttpResponse('notification_success')

        return HttpResponse('/notification_failure')

