from io import BytesIO
from datetime import datetime
from openpyxl.writer.excel import save_virtual_workbook
from django.http import HttpResponse
from django.shortcuts import render
from .read_write_xlsx_file import read_sheet, write_sheet


def home(request):
    return render(request, 'index.html')


def read_file(request):
    if request.method == 'POST' and request.FILES:
        request_file = request.FILES
        my_file = request_file['my_file']
        filename = BytesIO(my_file.read())

    # Read sheet
    read_sheet(filename)

    # Write on sheet
    wb = write_sheet(filename)

    MDATA = datetime.now().strftime('%Y-%m-%d-%H%M%S')

    # Use save_virtual_workbook...
    # content_type = 'application/vnd.ms-excel'
    # response = HttpResponse(
    #     save_virtual_workbook(wb),
    #     content_type=content_type
    # )

    # Or
    content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response = HttpResponse(content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename=file_{MDATA}.xlsx'

    wb.save(response)

    return response
