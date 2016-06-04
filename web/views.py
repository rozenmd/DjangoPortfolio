from subprocess import Popen
import subprocess
from django.views.generic import TemplateView, View
from django.http import StreamingHttpResponse, Http404
from wsgiref.util import FileWrapper
from DjangoPortfolio.settings import BASE_DIR
from web.forms import UrlsForm
from web.models import UrlRequest
from django.shortcuts import render
import re
from django.template.loader import render_to_string

import os
SCRIPT = BASE_DIR + '/static/js/rasterize.js'
PHANTOM = "/usr/lib/node_modules/phantomjs-prebuilt/lib/phantom/bin/phantomjs" #"/usr/local/bin/phantomjs"
OSX_PHANTOM = "/usr/local/lib/node_modules/phantomjs-prebuilt/lib/phantom/bin/phantomjs"

def phantom(request, url):
    outfile = BASE_DIR + '/test.pdf'
    params = [PHANTOM, SCRIPT, url, outfile]
    print (PHANTOM, SCRIPT, url, outfile)
    exitcode = subprocess.call(params)
    if exitcode == 0:
        return_file = FileWrapper(open(outfile, 'r'))
        download_file_name = 'output-pdf'
        response = StreamingHttpResponse(return_file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename= %s.pdf' % download_file_name
        return response
    else:
        return None


def urls_view(request, template="web/phantom.html"):
    form = UrlsForm()
    if request.method == 'POST':
        form = UrlsForm(request.POST)
        if form.is_valid():
            url = str(request.POST.get('url'))
            if re.search(r'^(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)', url):
                temp = UrlRequest(url=url)
                temp.save()
                return phantom(request, url)
            else:
                return render(request, template, {'form': form, 'errors': 'URL did not resolve'})

    return render(request, template, {'form': form})

