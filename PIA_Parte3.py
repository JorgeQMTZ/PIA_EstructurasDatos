import pandas as pd
csv_data = pd.read_csv("pacientes.csv", sep = ",")
csv_data.to_json("pacientes.json")

print("El archivo se ha exportado y convertido a un JSON")