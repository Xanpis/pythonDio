
texto = input('Digite o testo = ')
VOGAL = 'A-E-I-O-U'


for i in texto:
    if i.upper() in VOGAL:
        print(i.upper())
# Executa de qualquer forma depois de terminar o for  
else:
    print('Não Sao iguais ')