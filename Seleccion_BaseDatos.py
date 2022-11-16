import pyodbc

cnxn = pyodbc.connect("DSN=conexion")
cursor = cnxn.cursor()

print("--------------------------------")
print("Se ha conectado a la base de datos")
print("--------------------------------")

print("--------------------------------")
print("Se ha extraido la informacion de la base de datos")
print("--------------------------------")

cursor.execute('select * from Pacientes')

for fila in cursor.fetchall():
    print(fila)
    
cursor.close()
cnxn.close()

print("--------------------------------")
print("Se ha cerrado la base de datos")
print("--------------------------------")