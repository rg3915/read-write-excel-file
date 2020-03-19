import openpyxl
from datetime import datetime


MDATA = datetime.now().strftime('%Y-%m-%d-%H%M%S')


def read_sheet(filename):
    '''
    Read sheet and return a list of values.
    '''
    wb = openpyxl.load_workbook(filename)
    ws = wb['Sheet1']

    max_row = ws.max_row
    max_col = ws.max_column

    items = []

    for row in ws.iter_cols(max_col=max_col, max_row=max_row):
        sub_items = []
        for i, col in enumerate(row, 1):
            if i > 1:
                sub_items.append(col.value)
        items.append(sub_items)

    return items
