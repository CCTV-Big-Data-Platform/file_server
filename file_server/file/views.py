from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from .forms import UploadFileForm
from django.http import HttpResponse
import base64
import json
import os
from kafka import KafkaProducer
from kafka.errors import KafkaError

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print("---- data in ----")
            befEncoding = request.POST['befEncoding']
            userId = request.POST['userId']
            timeStamp = request.POST['timeStamp']
            encoded = befEncoding.encode()

            dict_data = {'data': befEncoding, 'userId': userId, 'timestamp': timeStamp}

            if not os.path.exists('./media/'+userId):
                os.makedirs('./media/'+userId)

            with open("media/"+userId+"/"+userId+"_"+timeStamp+".json", "w") as file:
                json.dump(dict_data, file, indent="\t")

            producer = KafkaProducer(bootstrap_servers=['1.201.142.81:9092'], max_request_size=52428800)

            future = producer.send('CCTV-stream', encoded)

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

