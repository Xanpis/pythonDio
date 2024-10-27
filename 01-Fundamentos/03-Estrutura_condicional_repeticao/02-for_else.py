
texto = input('Digite o testo = ')
VOGAL = 'AEIOU'


for i in texto:
    if i.upper() in VOGAL:
        print(i.upper())
# Executa de qualquer forma depois de terminar o for  
else:
    print('Não Sao iguais ')