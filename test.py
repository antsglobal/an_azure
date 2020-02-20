import pyodbc
server = 'numero.database.windows.net'
database = 'numero'
username = 'numero'
password = 'Alpha@123$'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT Temperature FROM ANIOT_TEMP")
row = cursor.fetchone()
while row:
    print (row[0])
    #print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()