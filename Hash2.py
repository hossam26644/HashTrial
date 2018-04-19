from hashlib import sha256
import xlrd
import xlwt
from xlutils.copy import copy


def mine(a, b, n1, n2, n3):
	for i in range (a,b):
		s = "winner is hossam, n="+str(i)
		h = sha256(s.encode())
		d = h.hexdigest()
		if d[0:n1]==("0"*n1):
			Out(d, i, n1)

		if d[0:n2]==("0"*n2):
			Out(d, i, n2)

		if d[0:n3]==("0"*n3):
			Out(d, i, n3)
			break
			
def Out(d,i,n):
	LogsWorkbook = xlrd.open_workbook("logs.xls") 
	LogsWorksheet = LogsWorkbook.sheet_by_index(0)
	LogsRowNumber = LogsWorksheet.nrows

	#wb = xlwt.Workbook()
	wb = copy(LogsWorkbook)
	s = wb.get_sheet(0)
	s.write(LogsRowNumber,0,str(d))
	s.write(LogsRowNumber,1,str(i))
	s.write(LogsRowNumber,2,str(n))


	print (d, i, n)


	wb.save("logs.xls")


mine(1,100000000,3,4,5)
