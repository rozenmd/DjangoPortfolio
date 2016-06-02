from subprocess import Popen
import subprocess
from django.views.generic import TemplateView, View
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
from DjangoPortfolio.settings import BASE_DIR
import os
SCRIPT = BASE_DIR + '/static/js/rasterize.js'
PHANTOM = "/usr/local/lib/node_modules/phantomjs-prebuilt/lib/phantom/bin/phantomjs" #"/usr/local/bin/phantomjs"
class MyPdfView(View):
    def get(self, request, *args, **kwargs):
        outfile = BASE_DIR + '/test.pdf'
        url = "http://www.codesource.com.au/"
        params = [PHANTOM, SCRIPT, url, outfile]
        exitcode = subprocess.call(params)
        if exitcode == 0:
            return_file = FileWrapper(open(outfile, 'r'))
            download_file_name = 'test'
            response = StreamingHttpResponse(return_file, content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename= %s.pdf' % download_file_name
            return response





