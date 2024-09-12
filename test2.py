from datetime import datetime, date, time, timezone

# datas_horas = datetime.now()
# print(datas_horas.strftime("%H:%M"))

datas_horas = datetime.now()
mascara_data_BR = datas_horas.strftime(" %d/%m/%y " "%H:%M")  
print(mascara_data_BR)