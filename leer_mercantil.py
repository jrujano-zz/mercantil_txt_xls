
import xlsxwriter


workbook = xlsxwriter.Workbook('Agosto-2019.xlsx') 
worksheet = workbook.add_worksheet() 

row = 0
column = 0
f = open("Agosto-2019.txt", 'r')


for linea in f.readlines():
	p_banco=linea.find(" ")
	banco=linea[0:4]
	p_moneda=linea.find(" ",p_banco+2)
	moneda=linea[7:10]
	cod_cuenta=linea[13:25]
	fecha=linea[26:34]
	cod_transaccion=linea[36:46]
	documento=linea[47:49]
	p_codigo_transaccion=linea.rfind(" ")
	p_monto_haber=linea.rfind(" ",0,p_codigo_transaccion-1)
	p_monto_debe=linea.rfind(" ",0,p_monto_haber-1)

	descripcion=linea[50:p_monto_debe-2]
	

	debe=linea[p_monto_debe+1:p_monto_haber].strip()
	haber=linea[p_monto_haber+1:p_codigo_transaccion].strip()
	debe_f=debe
	haber_f=haber
	len_linea=len(linea)
	#print(p_codigo_transaccion)	
	codigo_transaccion =linea[p_codigo_transaccion+1:len_linea]
	codigo_transaccion=codigo_transaccion.strip()
	#print("Debe : "+debe +" Haber: "+haber)	
	#print("codigo_transaccion :"+str(linea[p_codigo_transaccion:len(linea)]) +" monto_haber :"+str(linea[p_monto_haber:p_codigo_transaccion-1])+ " monto_debe :"+str(linea[p_monto_debe:p_monto_haber-1]))

	worksheet.write(row, 0, banco) 
	worksheet.write(row, 1, moneda) 
	worksheet.write(row, 2, cod_cuenta) 
	worksheet.write(row, 3, fecha)
	worksheet.write(row, 4, cod_transaccion)
	worksheet.write(row, 5, documento)
	worksheet.write(row, 6, descripcion)
	
	worksheet.write(row, 7, debe_f)
	worksheet.write(row, 8, haber_f)
	worksheet.write(row, 9, codigo_transaccion) 
	row += 1
f.close()
workbook.close() 