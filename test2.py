from datetime import datetime, date, time, timezone

# datas_horas = datetime.now()
# print(datas_horas.strftime("%H:%M"))
person = {}
while True:

    nome = input("nome: ")
    person[nome] = ""
    print(person)

    if nome == "0":
        break