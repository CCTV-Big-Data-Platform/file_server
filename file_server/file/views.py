from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from .forms import UploadFileForm
from django.http import HttpResponse
import base64
import json

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print("---- data in ----")
            befEncoding = request.POST['befEncoding']
            userId = request.POST['userId']
            timeStamp = request.POST['timeStamp']
            # bytesLike = bytes(befEncoding, encoding='utf8')
            # print("BYTES : ", bytesLike)
            # encoded_string = base64.b64encode(bytesLike)
            # print("Hey : ", encoded_string)

            json_data = json.dumps({'data': befEncoding, 'userId': userId , 'timestamp' : timeStamp})
            with open("media/"+userId+"/"+userId+"_"+timeStamp+".json", "w") as file:
                json.dump(json_data,file,indent="\t")
            print("---- process exit ----")

            return HttpResponse('save_success')
        else:
          form = UploadFileForm()
        # return render(request, 'upload.html', {'form': form})
        return HttpResponse('/upload_failure')
