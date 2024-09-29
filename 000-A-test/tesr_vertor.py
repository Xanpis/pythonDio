

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