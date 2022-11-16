import pyodbc
cnxn = pyodbc.connect("DSN=conexion")
cursor = cnxn.cursor()
cursor.tables()

rows = cursor.fetchall()


for row in rows:
    print(row.table_name)

print("--------------------------------")
print("Se ha conectado a la base de datos")
print("--------------------------------")

cursor.close()
cnxn.close()

print("--------------------------------")
print("Se ha cerrado la base de datos")
print("--------------------------------")