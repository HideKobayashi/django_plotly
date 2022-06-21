import os
from fileinput import filename
from django.shortcuts import render
from django.views.generic import TemplateView
from pathlib import Path
from django.conf import settings
from django.http import FileResponse

MEDIA_ROOT = Path(settings.BASE_DIR) / 'media'

class FileDownloadView(TemplateView):
    template_name = "fdlapp/filedownload.html"

    def get_context_data(self, **kwargs):
        self.file_path_list = list(MEDIA_ROOT.glob("*"))
        self.file_path_list.sort(key=os.path.getmtime, reverse=True)
        filelist = self.file_path_list
        context = super(FileDownloadView, self).get_context_data(**kwargs)
        context["filelist"] = filelist
        context["checked_list"] = filelist[:1]
        context["message"] = 'Get'
        return context

    def post(self, request, *args, **kwargs):
        file_name = request.POST.get("form_radio")
        file_path_name = os.path.join(MEDIA_ROOT, file_name)
        print("file_path_name:", file_path_name)
        return FileResponse(open(file_path_name, "rb"), as_attachment=True, filename=file_name)
    