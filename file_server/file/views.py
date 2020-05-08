from django.http import HttpResponseRedirect
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
          form = UploadFileForm(request.POST, request.FILES)
          if form.is_valid():
              userName = request.POST['userName']
              form.save()

              return HttpResponseRedirect('/success/url/')
        else:
          form = UploadFileForm()
        # return render(request, 'upload.html', {'form': form})
        return HttpResponseRedirect('/failure/url/')