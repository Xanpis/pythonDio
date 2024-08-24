# Convertendo para inteiro
num = 5.0
print(int(num)) 

# Uma (/) vira flutuante duas (//) fica inteiro mas não vira inteiro
num2 = 10
print(num2 /2 )
print(num2 //2 )

# Convertendo string
print(str(num))

# Concatenando 
nome = f"idade: {num2}, nome: Guilherme "
print(nome)

# Convertendo string para numero se tiver letra não converte
frute = '45'
print(int(frute))

print(int("10.10"))