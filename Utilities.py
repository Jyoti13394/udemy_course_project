from openpyxl import load_workbook


class Utilities:

    def data_from_excel_to_dict(path):
        data_dict = {}
        wb = load_workbook(path)
        sheet = wb.active
        rows = sheet.max_row
        for i in range(1, rows+1):
            #cell_obj = sheet.cell(row=i, column=1)
            data_dict[sheet.cell(row=i, column=1).value] = sheet.cell(row=i, column=2).value
        return data_dict
