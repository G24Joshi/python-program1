import openpyxl
wb=openpyxl.Workbook()
sheet=wb.active
sheet['A1']="Ramesh"
sheet['A2']="Raghav"
wb.save("myexecl2.xlsx")
