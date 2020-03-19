import openpyxl
from random import randint


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


def write_sheet(filename):
    '''
    Write on sheet.
    '''
    wb = openpyxl.load_workbook(filename)
    ws = wb['Sheet1']

    max_row = ws.max_row

    for row in ws.iter_rows(min_col=3, max_col=3, min_row=2, max_row=max_row):
        row[0].value = randint(1, 10)

    return wb
