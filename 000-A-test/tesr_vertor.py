
vet = [1,2,3,4,5,6,7,8,9,10]

p = len(vet) 
c = [] 
while True:
  p -=1
  c.append(vet[p]) 
  if p == 0:
      break
print("C: ",c)


d=[]
for i in range(len(vet), 0, -1):
    d.append(i)

print('D: ',d)

e = []
for i in reversed(vet):
    e.append(i)
    
print('E: ',e)


vet1 = [1,2,3,4,5,6,7,8,9,10]
vet2 = [1,2,3,4,5,6,7,8]

p = []
for i in range(10):
    
    if i < len(vet1):
        p.append(vet1[i])
        
    if i < len(vet2):
        p.append(vet2[i])

print(p)

# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.