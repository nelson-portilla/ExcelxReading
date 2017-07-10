from openpyxl import load_workbook
wb2 = load_workbook(filename='file.xlsx', read_only=True)
# print wb2.get_sheet_names()
# print wb2['ENTRADAS DIC']
ws = wb2['ENTRADAS DIC']
for row in ws.rows:
	print row
	for cell in row:
		print ""
		None    	
    	# if cell.value is not None:
	    #     #print(cell.value)