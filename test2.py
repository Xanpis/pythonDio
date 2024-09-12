from datetime import datetime, date, time, timezone, tzinfo
from time import strptime

# datas_horas = datetime.now()
# print(datas_horas.strftime("%H:%M"))
# person = {}
# while True:

#     nome = input("nome: ")
#     person[nome] = ""
#     print(person)

#     if nome == "0":
#         break

data_hora= datetime.now()
print(f" Data{data_hora.strftime(" %d/%m/%y ")} Hora:{data_hora.strftime(" %H:%M ")}")