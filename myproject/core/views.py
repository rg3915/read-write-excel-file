import tempfile
from io import BytesIO
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .read_write_xlsx_file import read_sheet


def home(request):
    return render(request, 'index.html')


def read_file(request):
    if request.method == 'POST' and request.FILES:
        request_file = request.FILES
        my_file = request_file['my_file']
        filename = BytesIO(my_file.read())

    with tempfile.NamedTemporaryFile(suffix='.xlsx') as tmp:
        items = read_sheet(filename)
        tmp.flush()
        tmp.seek(0)
        # data = tmp.read()
        data = items
        print(items)

    return HttpResponseRedirect(reverse('core:home'))
