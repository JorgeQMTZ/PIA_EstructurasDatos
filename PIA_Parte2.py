import pandas as pd
import random

pacientes= {"Paciente 1":[123, "Emilio Rodriguez", 45,"TOC"],
            "Paciente 2":[345, "María Ángeles Martínez", 56, "TOC"],
            "Paciente 3":[565, "Victorio López Ceballos", 34, "TDP"],
            "Paciente 4":[678, "Angela Armendáriz Alonso", 40, "TDP"],
            "Paciente 5":[456, "Carlos Gutiérrez Gonzales", 20, "TD"]
            }
pacientes = pd.DataFrame(pacientes)
pacientes.index = ["ID", "Nombre", "Edad","Tipo"]

pacientes.to_csv(r'pacientes.csv', index=True, header=True)
print("Se ha creado el CSV")