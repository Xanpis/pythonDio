from datetime import date, datetime, time, timedelta

data = date(2023, 7, 10)
print(data)
print(date.today())

data_hora = datetime(2023, 7, 10,)
print(data_hora)
print(datetime.today())

hora = time(10, 20, 0)  
print(hora)

hora_min_seg = datetime.now()
hora = hora_min_seg.hour
min = hora_min_seg.minute
seg = hora_min_seg.second

print(f"H:{hora} M:{min} S:{seg}")

