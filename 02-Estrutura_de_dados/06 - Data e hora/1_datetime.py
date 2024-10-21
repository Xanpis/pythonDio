from datetime import date, datetime, time, timedelta

# Na função data()  Eu passo um inteiro nos parâmetros e ela converte para OBJ tipo data,
data = date(2023, 7, 10)
print(data)
print(date.today())
print(30 * '=')

# Retorna um obj  data, hora, segundos, e minutos
print(datetime.today())
print(30 * '=')

# Retorna um obj do tipo hora mas só o que for passado por parâmetro, não retorna o atual  
hora = time(10, 20, 0)  
print(hora)
print(30 * '=')

# Pegando os horários atuais 
hora_min_seg = datetime.now()
hora = hora_min_seg.hour
min = hora_min_seg.minute
seg = hora_min_seg.second

print(f"H:{hora} M:{min} S:{seg}")

