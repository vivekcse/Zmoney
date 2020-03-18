import openpyxl

path = "C:\\Users\\vivek.yadav\\PycharmProjects\\weInvest\\drivers\\test2.xlsx"

workbook = openpyxl.load_workbook(path)
sheet = workbook.active

for r in range(1, 18):
    for c in range(1,12):
        sheet.cell(row=r, column=c).value = 'welcome' ' Vivek'

workbook.save(path)