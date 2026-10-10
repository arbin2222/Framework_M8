from xlrd import *


wb=open_workbook('test_data/excel_data.xlsx')
sheet=wb.sheet_by_name("Sheet1")


def get_valid_test_data():
    rows=sheet.row_values(1)   #rows=[1,'standard_user','secret_sauce']
    un=rows[1]
    pwd=rows[2]
    return un,pwd





def get_invalid_test_data():
    rows=sheet.row_values(2)     #rows=[2,'arbin','123456']
    un=rows[1]
    pwd=rows[2]
    return un,pwd
