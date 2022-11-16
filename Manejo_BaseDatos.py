import pyodbc

cnxn = pyodbc.connect("DSN=conexion")
cursor = cnxn.cursor()

cursor.execute("insert into Pacientes(identificacion, nombre, apellidos, edad, tipo) values('123','Emilio','Rodriguez',45,'TOC')")
cursor.execute("insert into Pacientes(identificacion, nombre, apellidos, edad, tipo) values('345','Maria Angeles',' Martinez',56,'TOC')")
cursor.execute("insert into Pacientes(identificacion, nombre, apellidos, edad, tipo) values('565','Victorio','Lopez Ceballos',34,'TMP')")
cursor.execute("insert into Pacientes(identificacion, nombre, apellidos, edad, tipo) values('678','Angela','Armendariz Alonso',40,'TMP')")
cursor.execute("insert into Pacientes(identificacion, nombre, apellidos, edad, tipo) values('456','Carlos','Guitierrez Gonzales',20,'TPD')")

cnxn.commit()

print("--------------------------------")
print("Se ha conectado a la base de datos")
print("--------------------------------")

print("--------------------------------")
print("Se han insertado los campos dentro de la base de datos")
print("--------------------------------")

cursor.close()
cnxn.close()

print("--------------------------------")
print("Se ha cerrado la base de datos")
print("--------------------------------")