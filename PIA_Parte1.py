pacientes= {"Paciente 1":[123, "Emilio Rodriguez", 45,"TOC"],
            "Paciente 2":[345, "María Ángeles Martínez", 56, "TOC"],
            "Paciente 3":[565, "Victorio López Ceballos", 34, "TDP"],
            "Paciente 4":[678, "Angela Armendáriz Alonso", 40, "TDP"],
            "Paciente 5":[456, "Carlos Gutiérrez Gonzales", 20, "TD"]
            }

print("La lista de pacientes es: ")
print(pacientes["Paciente 1"])
print(pacientes["Paciente 2"])
print(pacientes["Paciente 3"])
print(pacientes["Paciente 4"])
print(pacientes["Paciente 5"])
print("---------------------------------")
print("El numero de pacientes es: ")
print(len(pacientes))
print("---------------------------------")
print("Se agrega un nuevo paciente: ")
pacientes["Paciente 6"]=765, "Juan Galvan Ortiz", 34, "TD"
print(pacientes["Paciente 6"])
print("---------------------------------")
print("Se eliminara el nuevo paciente por cancelacion")
del pacientes ["Paciente 6"]
print("La lista definitiva para mañana")
print(pacientes)
print("---------------------------------")
print("FIN")
print("---------------------------------")

