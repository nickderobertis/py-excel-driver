from openpyxl import load_workbook


def _load_workbook_and_worksheet(filepath):
    wb = load_workbook(filepath)
    ws = wb.active

    return wb, ws