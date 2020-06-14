from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from .forms import UploadFileForm
from django.http import HttpResponse
import base64
import json
import os
from kafka import KafkaProducer
from kafka.errors import KafkaError

"""
File Upload View는 전송받은 프레임 데이터를 카프카에 프로듀스하는 클래스입니다. 
post api를 안드로이드에서 호출하면 해당 데이터를 jsong Object를 str으로 dumps하여 프로듀스 진행합니다.
"""
class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    tog = True

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print("---- data in ----")
            befEncoding = request.POST['befEncoding']
            userId = request.POST['userId']
            timeStamp = request.POST['timeStamp']

            dict_data = {'data': befEncoding, 'userId': userId, 'timestamp': timeStamp}

            if not os.path.exists('./media/'+userId):
                os.makedirs('./media/'+userId)

            with open("media/"+userId+"/"+userId+"_"+timeStamp+".json", "w") as file:
                json.dump(dict_data, file, indent="\t")

            producer = KafkaProducer(bootstrap_servers=['1.201.142.81:9092'], max_request_size=209717600)
            jsonObject = json.dumps(dict_data).encode('utf-8')
            global tog
            FileUploadView.tog = self.toggle( FileUploadView.tog)
            # print(type(FileUploadView.tog))
            # if FileUploadView.tog == True:
            #     future = producer.send('test4', jsonObject)
            # elif FileUploadView.tog == False:
            #     future = producer.send('test98', jsonObject)

            future = producer.send('test4', jsonObject)
            try:
                record_metadata = future.get(timeout=10)
            except KafkaError as err:
                # Decide what to do if produce request failed…
                print(err)
                # log.exception()
                pass

            # Successful result returns assigned partition and offset
            print("TOPIC : ", record_metadata.topic)
            print("Partition :", record_metadata.partition)
            print("Offset : ", record_metadata.offset)
            print("---- process exit ----")

            return HttpResponse('save_success')
        else:
          form = UploadFileForm()
        # return render(request, 'upload.html', {'form': form})
        return HttpResponse('/upload_failure')

    def toggle(self, tog):
        return not tog
